from django.contrib import admin
from .models import Group, Brand, Unit, Firm, Material, Project, ProjectMaterial


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
	list_display = ('name', 'firm', 'height', 'project_type', 'width_a', 'width_b', 'width_c', 'width_d',
					'wall_area', 'room_area', 'living_room_area', 'ceiling_area')
	search_fields = ('name', 'firm__name')
	list_filter = ('project_type', 'firm')
	fieldsets = (
		(None, {
			'fields': ('name', 'firm', 'height', 'project_type')
		}),
		('Размеры стены', {
			'fields': ('width_a', 'width_b', 'width_c', 'width_d', 'wall_area',
					   'wall_area_a', 'wall_area_b', 'wall_area_c', 'wall_area_d'),
			'classes': ('collapse',)
		}),
		('Размеры комнаты', {
			'fields': ('room_area',),
		}),
		('Размеры гостиной', {
			'fields': ('living_room_area',),
		}),
		('Размеры потолка', {
			'fields': ('ceiling_area', 'ceiling_area_a', 'ceiling_area_b', 'ceiling_area_c', 'ceiling_area_d'),
			'classes': ('collapse',)
		}),
	)


@admin.register(ProjectMaterial)
class MaterialProjectAdmin(admin.ModelAdmin):
	list_display = ('project', 'material', 'type_material',)
	list_filter = ('type_material',)
