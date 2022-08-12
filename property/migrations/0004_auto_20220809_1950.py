# Generated by Django 2.2.24 on 2022-08-09 16:50

from django.db import migrations

def fill_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    new_flats = Flat.objects.filter(construction_year__gt=2015)
    new_flats.update(new_building=True)
    old_flats = Flat.objects.filter(construction_year__lt=2015)
    old_flats.update(new_building=False)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_field)
    ]
