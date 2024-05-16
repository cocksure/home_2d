from django import forms
from django.forms import inlineformset_factory

from info.models import Group, Brand, Firm, Material, Unit, Project, ProjectMaterial


class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
		}


class BrandForm(forms.ModelForm):
	class Meta:
		model = Brand
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
		}


class FirmForm(forms.ModelForm):
	class Meta:
		model = Firm
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
		}


class UnitForm(forms.ModelForm):
	class Meta:
		model = Unit
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
		}


class MaterialForm(forms.ModelForm):
	class Meta:
		model = Material
		fields = ['name', 'group', 'brand', 'price', 'unit', 'norm', ]
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'group': forms.Select(attrs={'class': 'form-control'}),
			'brand': forms.Select(attrs={'class': 'form-control'}),
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
			'unit': forms.Select(attrs={'class': 'form-control'}),
			'norm': forms.NumberInput(attrs={'class': 'form-control'}),
		}


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ['wall_area', 'ROOM_area', 'LIVING_ROOM_area']

		fields = '__all__'

		labels = {
			'name': '',
			'firm': 'Фирма',
			'project_type': 'Тип проекта',
			'height': '',
			'width_a': '',
			'width_b': '',
			'width_c': '',
			'width_d': '',

		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
			'firm': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Фирма'}),
			'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Высота'}),
			'project_type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Тип проекта'}),
			'width_a': forms.NumberInput(
				attrs={'class': 'form-control', 'id': 'id_width_a', 'placeholder': 'Ширина A'}),
			'width_b': forms.NumberInput(
				attrs={'class': 'form-control', 'id': 'id_width_b', 'placeholder': 'Ширина B'}),
			'width_c': forms.NumberInput(
				attrs={'class': 'form-control', 'id': 'id_width_c', 'placeholder': 'Ширина C'}),
			'width_d': forms.NumberInput(
				attrs={'class': 'form-control', 'id': 'id_width_d', 'placeholder': 'Ширина D'}),

		}


class ProjectMaterialForm(forms.ModelForm):
	class Meta:
		model = ProjectMaterial
		fields = ['material', 'type_material']
		widgets = {
			'material': forms.Select(
				attrs={'class': 'form-select material mb-3', 'id': 'material', 'name': 'material', }),
			'type_material': forms.Select(
				attrs={'class': 'form-select type_material', 'id': 'type_material', 'name': 'type_material', }),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['material'].queryset = Material.objects.all()


ProjectMaterialFormSet = inlineformset_factory(Project, ProjectMaterial, form=ProjectMaterialForm, extra=1)
