# Generated by Django 5.0.1 on 2024-01-31 16:53

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('angeline', '0006_alter_completecadastro_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completecadastro',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
