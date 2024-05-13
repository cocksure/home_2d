from django.urls import path

from info.views import base_html_view, FirmListCreate, GroupListCreate, BrandListCreate, MaterialListCreate, \
	UnitListCreate, ProjectListCreate

urlpatterns = [
	path('', base_html_view, name='base_html'),

	path('firms/', FirmListCreate.as_view(), name='firm-list'),
	path('groups/', GroupListCreate.as_view(), name='group-list'),
	path('brands/', BrandListCreate.as_view(), name='brand-list'),
	path('units/', UnitListCreate.as_view(), name='unit-list'),
	path('materials/', MaterialListCreate.as_view(), name='material-list'),
	path('project/', ProjectListCreate.as_view(), name='project-list'),

]
