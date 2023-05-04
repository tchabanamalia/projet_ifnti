# Generated by Django 4.2.1 on 2023-05-04 07:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_matiere_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='datenaissance',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2006, 1, 1), message="L'année de naissance doit être inférieure à 2006")], verbose_name='date de naissance'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='datenaissance',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2006, 1, 1), message="L'année de naissance doit être inférieure à 2006")], verbose_name='date de naissance'),
        ),
    ]
