# Generated by Django 4.2 on 2023-05-04 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diet', '0002_alter_diet_description_alter_diet_duration_in_weeks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
