# Generated by Django 5.0.6 on 2024-05-14 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_alter_projectmaterial_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='LIVING_ROOM_area',
            new_name='living_room_area',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='ROOM_area',
            new_name='room_area',
        ),
    ]
