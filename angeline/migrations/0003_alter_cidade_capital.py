# Generated by Django 5.0.1 on 2024-01-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angeline', '0002_cidade_capital_cidade_codigo_uf_cidade_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='capital',
            field=models.BooleanField(default=False),
        ),
    ]
