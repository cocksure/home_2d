from django.shortcuts import render

from info.forms import FirmForm, GroupForm, UnitForm, MaterialForm, ProjectForm, BrandForm
from info.models import Firm, Group, Brand, Unit, Material, Project
from shared.views import BaseListCreateView


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


class ProjectListCreate(BaseListCreateView):
	model = Project
	form_class = ProjectForm
	template_name = "project_list_create.html"
	redirect_url = "project-list"
