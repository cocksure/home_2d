# Generated by Django 5.0.6 on 2024-05-15 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_project_full_area_alter_project_ceiling_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='full_area',
        ),
    ]
