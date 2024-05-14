from django import forms
from info.models import Group, Brand, Firm, Material, Unit, Project


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
		exclude = ['wall_area', 'ROOM_area', 'LIVING_ROOM_area']  # isklyuchit' polya iz formy

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
			'interior_walls': 'Внутренние стены',
			'external_walls': 'Внешние стены',
			'floor': 'Пол',
			'baseboard': 'Паталок',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
			'firm': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Фирма'}),
			'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Высота'}),
			'project_type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Тип проекта'}),
			'material': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Материал'}),
			'width_a': forms.NumberInput(
				attrs={'class': 'form-control', 'id': 'id_width_a', 'placeholder': 'Ширина A'}),
			'width_b': forms.NumberInput(
				attrs={'class': 'form-control', 'id': 'id_width_b', 'placeholder': 'Ширина B'}),
			'width_c': forms.NumberInput(
				attrs={'class': 'form-control', 'id': 'id_width_c', 'placeholder': 'Ширина C'}),
			'width_d': forms.NumberInput(
				attrs={'class': 'form-control', 'id': 'id_width_d', 'placeholder': 'Ширина D'}),
			'interior_walls': forms.CheckboxInput(attrs={'class': 'form-check-input custom-checkbox'}),
			'external_walls': forms.CheckboxInput(attrs={'class': 'form-check-input custom-checkbox'}),
			'floor': forms.CheckboxInput(attrs={'class': 'form-check-input custom-checkbox'}),
			'baseboard': forms.CheckboxInput(attrs={'class': 'form-check-input custom-checkbox'}),
		}
