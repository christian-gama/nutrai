# Generated by Django 4.2 on 2023-05-03 13:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(
                    1), django.core.validators.MaxValueValidator(150)])),
                ('weight_kg', models.DecimalField(decimal_places=2, max_digits=5,
                 validators=[django.core.validators.MinValueValidator(1.0)])),
                ('height_m', models.DecimalField(decimal_places=2, max_digits=4,
                 validators=[django.core.validators.MinValueValidator(1.0)])),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
