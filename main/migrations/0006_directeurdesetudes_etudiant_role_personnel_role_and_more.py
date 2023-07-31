# Generated by Django 4.2.3 on 2023-07-25 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_merge_20230725_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirecteurDesEtudes',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.personnel')),
                ('actif', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Directeur des études',
                'verbose_name_plural': 'Directeurs des études',
            },
            bases=('main.personnel',),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='role',
            field=models.CharField(default='User', max_length=50),
        ),
        migrations.AddField(
            model_name='personnel',
            name='role',
            field=models.CharField(default='User', max_length=50),
        ),
        migrations.AlterField(
            model_name='fichedepaie',
            name='niveau1',
            field=models.CharField(choices=[('semestre1', 'S1'), ('semestre2', 'S2')], max_length=30),
        ),
        migrations.AlterField(
            model_name='fichedepaie',
            name='niveau2',
            field=models.CharField(choices=[('semestre3', 'S3'), ('semestre4', 'S4')], max_length=30),
        ),
        migrations.AlterField(
            model_name='fichedepaie',
            name='niveau3',
            field=models.CharField(choices=[('semestre5', 'S5'), ('semestre6', 'S6')], max_length=30),
        ),
        migrations.AlterField(
            model_name='fichedepaie',
            name='prixUnitaire',
            field=models.IntegerField(default=2000, verbose_name='Prix unitaire'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='id',
            field=models.CharField(blank=True, max_length=12, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200)),
                ('date_et_heure_debut', models.DateTimeField()),
                ('date_et_heure_fin', models.DateTimeField()),
                ('description', models.TextField()),
                ('valider', models.BooleanField(default=False)),
                ('auteur', models.ForeignKey(default='Anonyme', on_delete=django.db.models.deletion.CASCADE, related_name='seance_auteur', to='main.etudiant')),
                ('eleves_presents', models.ManyToManyField(related_name='seances_presents', to='main.etudiant')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.matiere')),
            ],
        ),
    ]