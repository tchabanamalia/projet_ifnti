# Generated by Django 4.0.1 on 2023-05-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_etudiant_is_admis_alter_etudiant_semestre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='is_admis',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='passer_semestre_suivant',
            field=models.BooleanField(default=False, verbose_name='Passer au semestre suivant'),
        ),
    ]
