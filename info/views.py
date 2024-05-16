from xhtml2pdf import pisa
from io import BytesIO

from django.db import transaction
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from info.forms import FirmForm, GroupForm, UnitForm, MaterialForm, ProjectForm, BrandForm, ProjectMaterialFormSet
from info.models import Firm, Group, Brand, Unit, Material, Project, ProjectMaterial
from shared.views import BaseListCreateView, BaseListView


def base_html_view(request):
	return render(request, 'base.html')


class FirmListCreate(BaseListCreateView):
	model = Firm
	form_class = FirmForm
	template_name = "firm_list_create.html"
	redirect_url = "firm-list"


class GroupListCreate(BaseListCreateView):
	model = Group
	form_class = GroupForm
	template_name = "group_list_create.html"
	redirect_url = "group-list"


class BrandListCreate(BaseListCreateView):
	model = Brand
	form_class = BrandForm
	template_name = "brand_list_create.html"
	redirect_url = "brand-list"


class UnitListCreate(BaseListCreateView):
	model = Unit
	form_class = UnitForm
	template_name = "unit_list_create.html"
	redirect_url = "unit-list"


class MaterialListCreate(BaseListCreateView):
	model = Material
	form_class = MaterialForm
	template_name = "material_list_create.html"
	redirect_url = "material-list"


class ProjectListView(BaseListView):
	model = Project
	form_class = None
	template_name = "project_list.html"

	def get(self, request):
		projects = self.get_queryset()
		page_obj = self.apply_pagination_and_search(projects, request)
		context = {
			'items': page_obj,
		}
		return render(request, self.get_template_name(), context)


class ProjectCreateView(CreateView):
	model = Project
	form_class = ProjectForm
	template_name = "project_list_create.html"

	def form_valid(self, form):
		project = form.save(commit=False)

		try:
			with transaction.atomic():
				project.save()

				detail_counter = int(self.request.POST.get('detail_counter', 0))

				for detail_index in range(1, detail_counter + 1):
					material_id = self.request.POST.get('material_' + str(detail_index))
					type_material = self.request.POST.get('type_material_' + str(detail_index))
					if material_id and type_material:
						material = Material.objects.get(id=material_id)
						project_material = ProjectMaterial.objects.create(
							material=material,
							type_material=type_material,
							project=project
						)
						project_material.summa = project_material.calculate_summa()
						project_material.save()

		except Exception as e:

			return JsonResponse({'error': str(e)}, status=400)
		else:

			return HttpResponseRedirect(reverse_lazy('project-list'))

	def form_invalid(self, form):
		return JsonResponse({'success': False, 'errors': form.errors}, status=400)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.object:
			context['project_material_formset'] = ProjectMaterialFormSet(
				self.request.POST if self.request.method == 'POST' else None,
				instance=self.object
			)
		else:
			context['project_material_formset'] = ProjectMaterialFormSet()
		return context


class ProjectDetailView(DetailView):
	model = Project
	template_name = 'project_detail.html'
	context_object_name = 'project'
	form_class = ProjectForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		project = self.get_object()
		project_materials = project.project_materials.all()  # Здесь исправление
		form = self.form_class()
		context['project_materials'] = project_materials
		context['form'] = form
		return context


import matplotlib.pyplot as plt


def create_pdf_view(request, pk):
	project = Project.objects.get(pk=pk)
	project_materials = project.project_materials.all()  # Получаем все связанные материалы

	# Создаем чертеж с помощью Matplotlib
	fig, ax = plt.subplots(figsize=(11.69, 8.27))  # A4 landscape

	# Рисуем только стены A и B
	if project.width_a:
		ax.plot([0, project.width_a], [0, 0], label='Стена A', linestyle='-', marker='o')
	if project.width_b:
		ax.plot([project.width_a, project.width_a], [0, project.width_b], label='Стена B', linestyle='-', marker='o')

	ax.set_aspect('equal')
	ax.legend()
	ax.set_title('Планировка проекта')
	ax.set_xlabel('Длина, м')
	ax.set_ylabel('Ширина, м')

	# Сохраняем изображение на диск
	img_path = f'/tmp/project_{pk}_plan.png'  # Путь к файлу
	plt.savefig(img_path, format='png')
	plt.close()

	# Создаем шаблон PDF
	template_path = 'pdf_template.html'

	# Передаем путь к изображению и материалы в контекст
	context = {
		'project': project,
		'project_plan_image': img_path,
		'project_materials': project_materials
	}

	# Загружаем HTML-шаблон
	template = get_template(template_path)
	html = template.render(context)

	# Создаем буфер для записи PDF
	pdf_buffer = BytesIO()

	# Создаем PDF из HTML-кода
	pisa.CreatePDF(BytesIO(html.encode('UTF-8')), pdf_buffer, pagesize='A4', encoding='UTF-8')

	# Сбрасываем указатель файлового объекта на начало
	pdf_buffer.seek(0)

	# Отправляем PDF в ответе
	response = HttpResponse(pdf_buffer, content_type='application/pdf')
	response['Content-Disposition'] = f'filename="project_{pk}_plan.pdf"'
	return response
