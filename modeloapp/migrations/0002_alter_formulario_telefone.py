# Generated by Django 4.0.5 on 2022-07-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeloapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='telefone',
            field=models.CharField(max_length=11),
        ),
    ]
