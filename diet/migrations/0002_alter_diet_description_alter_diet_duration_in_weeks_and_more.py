# Generated by Django 4.2 on 2023-05-03 19:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='description',
            field=models.TextField(max_length=500, validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
        migrations.AlterField(
            model_name='diet',
            name='duration_in_weeks',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='diet',
            name='name',
            field=models.CharField(max_length=150, validators=[django.core.validators.MaxLengthValidator(150)]),
        ),
    ]
