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

	name = models.CharField(max_length=150)
	firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
	height = models.DecimalField(max_digits=10, decimal_places=2)
	project_type = models.CharField(choices=ProjectType.choices, default=ProjectType.WALL, max_length=20)
	width_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	width_b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	width_c = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	width_d = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	interior_walls = models.BooleanField(default=False, null=True, blank=True)
	external_walls = models.BooleanField(default=False, null=True, blank=True)
	floor = models.BooleanField(default=False, null=True, blank=True)
	baseboard = models.BooleanField(default=False, null=True, blank=True)

	def __str__(self):
		return str(self.name)
