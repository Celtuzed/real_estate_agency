# Generated by Django 2.2.24 on 2022-09-06 16:33
from ast import parse
import phonenumbers

from django.db import migrations

def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
            number = flat.owners_phonenumber
            parsed_number = phonenumbers.parse(number, 'RU')
            if phonenumbers.is_possible_number(parsed_number) and phonenumbers.is_valid_number(parsed_number):
                pure_phoennumber = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                flat.owner_pure_phone = pure_phoennumber
                flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220819_1849'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone, move_backward)
    ]
