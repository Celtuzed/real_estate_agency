# Generated by Django 2.2.24 on 2022-10-14 16:09

from django.db import migrations


def fill_owners_and_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        try:
            owner = Owner.objects.get(owner = flat.owner)
            owner.flat.set([flat.id])
            owner.save()
        except Owner.MultipleObjectsReturned:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20221014_1851'),
    ]

    operations = [
        migrations.RunPython(fill_owners_and_flats)
    ]
