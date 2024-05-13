from django.contrib import admin
from .models import Group, Brand, Unit, Firm, Material, Project


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
	list_display = ('name', 'group', 'brand', 'unit', 'price', 'norm')
	search_fields = ('name',)
	list_filter = ('group', 'brand', 'unit')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = (
	'name', 'firm', 'height', 'project_type', 'width_a', 'width_b', 'width_c', 'width_d', 'interior_walls',
	'external_walls', 'floor', 'baseboard')
	search_fields = ('name', 'firm__name')
	list_filter = ('project_type', 'firm')
