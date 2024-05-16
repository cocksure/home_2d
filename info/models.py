from decimal import Decimal

from django.db import models


class Group(models.Model):
	name = models.CharField(max_length=150, unique=True)

	def __str__(self):
		return str(self.name)


class Brand(models.Model):
	name = models.CharField(max_length=150, unique=True)

	def __str__(self):
		return str(self.name)


class Unit(models.Model):
	name = models.CharField(max_length=150, unique=True)

	def __str__(self):
		return str(self.name)


class Firm(models.Model):
	name = models.CharField(max_length=150, unique=True)

	def __str__(self):
		return str(self.name)


class Material(models.Model):
	name = models.CharField(max_length=150, unique=True)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	norm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def __str__(self):
		return str(self.name)


class Project(models.Model):
	class ProjectType(models.TextChoices):
		WALL = 'СТЕНА', 'СТЕНА'
		ROOM = 'КОМНАТА', 'КОМНАТА'
		LIVING_ROOM = 'ГОСТИННАЯ', 'ГОСТИННАЯ'

	name = models.CharField(max_length=150, verbose_name='Название')
	firm = models.ForeignKey('Firm', on_delete=models.CASCADE, verbose_name='Фирма')
	height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Высота')
	project_type = models.CharField(choices=ProjectType.choices, default=ProjectType.WALL, max_length=20,
									verbose_name='Тип проекта')

	width_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Ширина A')
	width_b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Ширина B')
	width_c = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Ширина C')
	width_d = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Ширина D')

	wall_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
									verbose_name='Общая Площадь стены')
	room_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
									verbose_name='Площадь комнаты')
	living_room_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
										   verbose_name='Площадь гостиной')

	wall_area_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
									  verbose_name='Площадь стены A')
	wall_area_b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
									  verbose_name='Площадь стены B')
	wall_area_c = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
									  verbose_name='Площадь стены C')
	wall_area_d = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
									  verbose_name='Площадь стены D')

	ceiling_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
									   verbose_name='Общая Площадь потолка')
	ceiling_area_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
										 verbose_name='Площадь потолка A')
	ceiling_area_b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
										 verbose_name='Площадь потолка B')
	ceiling_area_c = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
										 verbose_name='Площадь потолка C')
	ceiling_area_d = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
										 verbose_name='Площадь потолка D')

	def save(self, *args, **kwargs):
		if self.project_type == Project.ProjectType.WALL and self.width_a:
			self.wall_area = self.height * self.width_a
			self.wall_area_a = None
			self.wall_area_b = None
			self.wall_area_c = None
			self.wall_area_d = None
			self.room_area = None
			self.living_room_area = None
		elif self.project_type == Project.ProjectType.ROOM and self.width_a and self.width_b:
			self.room_area = (self.height * self.width_a) + (self.height * self.width_b) * 2
			self.wall_area = self.room_area
			self.wall_area_a = self.height * self.width_a
			self.wall_area_b = self.height * self.width_b
			self.wall_area_c = None
			self.wall_area_d = None
			self.living_room_area = None
		elif self.project_type == Project.ProjectType.LIVING_ROOM and all(
				[self.width_a, self.width_b, self.width_c, self.width_d]):
			self.living_room_area = (self.height * self.width_a) + (self.height * self.width_b) + \
									(self.height * self.width_c) + (self.height * self.width_d) * 2
			self.wall_area = self.living_room_area
			self.wall_area_a = self.height * self.width_a
			self.wall_area_b = self.height * self.width_b
			self.wall_area_c = self.height * self.width_c
			self.wall_area_d = self.height * self.width_d
			self.room_area = None
		else:
			self.wall_area = None
			self.wall_area_a = None
			self.wall_area_b = None
			self.wall_area_c = None
			self.wall_area_d = None
			self.room_area = None
			self.living_room_area = None

		# Расчет общей площади потолка
		self.ceiling_area_a = self.width_a * self.width_b if self.width_a and self.width_b else None
		self.ceiling_area_b = self.width_b * self.width_c if self.width_b and self.width_c else None
		self.ceiling_area_c = self.width_c * self.width_d if self.width_c and self.width_d else None
		self.ceiling_area_d = self.width_d * self.width_a if self.width_d and self.width_a else None

		self.ceiling_area = sum(filter(None, [
			self.ceiling_area_a, self.ceiling_area_b, self.ceiling_area_c, self.ceiling_area_d
		]))

		super().save(*args, **kwargs)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ['-id']


class ProjectMaterial(models.Model):
	class MaterialType(models.TextChoices):
		INTERIOR_WALLS = 'ВНУТРЕННИЕ СТЕНЫ', 'ВНУТРЕННИЕ СТЕНЫ'
		EXTERNAL_WALLS = 'ВНЕШНИЕ СТЕНЫ', 'ВНЕШНИЕ СТЕНЫ'
		FLOOR = 'ПОЛ', 'ПОЛ'
		BASEBOARD = 'ПАТАЛОК', 'ПАТАЛОК'

	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_materials')
	material = models.ForeignKey(Material, on_delete=models.CASCADE)
	type_material = models.CharField(choices=MaterialType.choices, max_length=20, blank=True)
	summa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def calculate_summa(self):
		if self.type_material in [self.MaterialType.INTERIOR_WALLS, self.MaterialType.EXTERNAL_WALLS]:
			if self.material.norm is not None and self.project.wall_area is not None:
				return self.material.norm * self.project.wall_area
			else:
				return Decimal('0.0')
		elif self.type_material in [self.MaterialType.FLOOR, self.MaterialType.BASEBOARD]:
			if self.material.norm is not None and self.project.ceiling_area is not None:
				return self.material.norm * self.project.ceiling_area
			else:
				return Decimal('0.0')
		else:
			return Decimal('0.0')

	def __str__(self):
		return f"{self.material.name}  {self.type_material}"
