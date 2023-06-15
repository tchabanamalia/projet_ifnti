# Generated by Django 4.2.2 on 2023-06-08 12:24

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeUniversitaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anneeUniv', models.CharField(max_length=300, verbose_name='Année universitaire')),
                ('anneeUnivCourante', models.BooleanField(default=False, null=True, verbose_name='Année universitaire acutuelle')),
            ],
        ),
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255, verbose_name='Libelle')),
                ('description', models.TextField(max_length=500, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50, verbose_name='Prénom')),
                ('sexe', models.CharField(choices=[('F', 'Feminin'), ('M', 'Masculin')], max_length=1)),
                ('datenaissance', models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2006, 1, 1), message="L'année de naissance doit être inférieure à 2006")], verbose_name='date de naissance')),
                ('lieunaissance', models.CharField(blank=True, max_length=20, verbose_name='lieu de naissance')),
                ('contact', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50, null=True)),
                ('adresse', models.CharField(max_length=50)),
                ('prefecture', models.CharField(blank=True, default='tchaoudjo', max_length=50, null=True, verbose_name='Préfecture')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('carte_identity', models.CharField(max_length=50, null=True, verbose_name="Carte d'identité")),
                ('nationalite', models.CharField(blank=True, default='Togolaise', max_length=30, verbose_name='Nationalté')),
                ('id', models.CharField(blank=True, max_length=12, primary_key=True, serialize=False)),
                ('seriebac1', models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F1', 'F1'), ('F2', 'F2'), ('F3', 'F3'), ('F4', 'F4'), ('G2', 'G2')], max_length=2, null=True, verbose_name='Série bac 1')),
                ('seriebac2', models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F1', 'F1'), ('F2', 'F2'), ('F3', 'F3'), ('F4', 'F4'), ('G2', 'G2')], max_length=2, null=True, verbose_name='Série bac 2')),
                ('anneeentree', models.IntegerField(blank=True, default=2023, verbose_name='année entrée')),
                ('anneebac1', models.IntegerField(blank=True, null=True, verbose_name='Année d’obtention du BAC 1')),
                ('anneebac2', models.IntegerField(blank=True, default=2023, null=True, verbose_name='Année d’obtention du BAC 2')),
                ('etablissementSeconde', models.CharField(blank=True, max_length=300, null=True, verbose_name="Nom d'établissement seconde")),
                ('francaisSeconde', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name='Note de français Seconde')),
                ('anglaisSeconde', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name="Note d'anglais Seconde")),
                ('mathematiqueSeconde', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name='Note de mathématique Seconde')),
                ('etablissementPremiere', models.CharField(blank=True, max_length=300, null=True, verbose_name="Nom d'établissement Première")),
                ('francaisPremiere', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name='Note de français Première')),
                ('anglaisPremiere', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name="Note d'anglais Première")),
                ('mathematiquePremiere', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name='Note de mathématique Première')),
                ('etablissementTerminale', models.CharField(blank=True, max_length=300, null=True, verbose_name="Nom d'établissement Terminale")),
                ('francaisTerminale', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name='Note de français Terminale')),
                ('anglaisTerminale', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name="Note d'anglais Terminale")),
                ('mathematiqueTerminale', models.DecimalField(decimal_places=2, default='0', max_digits=4, verbose_name='Note de mathématique Terminale')),
            ],
            options={
                'verbose_name': 'Etudiant',
                'verbose_name_plural': 'Etudiants',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=258, verbose_name='Nom')),
                ('ponderation', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Pondération (%)')),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Parcours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255, verbose_name='Libelle')),
                ('description', models.TextField(max_length=500, verbose_name='description')),
                ('domaine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.domaine', verbose_name='Domaine')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50, verbose_name='Prénom')),
                ('sexe', models.CharField(choices=[('F', 'Feminin'), ('M', 'Masculin')], max_length=1)),
                ('datenaissance', models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2006, 1, 1), message="L'année de naissance doit être inférieure à 2006")], verbose_name='date de naissance')),
                ('lieunaissance', models.CharField(blank=True, max_length=20, verbose_name='lieu de naissance')),
                ('contact', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50, null=True)),
                ('adresse', models.CharField(max_length=50)),
                ('prefecture', models.CharField(blank=True, default='tchaoudjo', max_length=50, null=True, verbose_name='Préfecture')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('carte_identity', models.CharField(max_length=50, null=True, verbose_name="Carte d'identité")),
                ('nationalite', models.CharField(blank=True, default='Togolaise', max_length=30, verbose_name='Nationalté')),
                ('salaireBrut', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salaire Brut')),
                ('dernierdiplome', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Dernier diplome')),
                ('nbreJrsCongesRestant', models.IntegerField(verbose_name='Nonbre de jours de congé restant')),
                ('nbreJrsConsomme', models.IntegerField(verbose_name='Nonbre de jours consommé')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeUE', models.CharField(max_length=50, verbose_name="Code de l'UE")),
                ('libelle', models.CharField(max_length=100)),
                ('nbreCredits', models.IntegerField(verbose_name='Nombre de crédit')),
                ('heures', models.DecimalField(blank=True, decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name_plural': 'UE',
            },
        ),
        migrations.CreateModel(
            name='Comptable',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.personnel')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.personnel',),
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.personnel')),
                ('type', models.CharField(blank=True, choices=[('Vacataire', 'Vacataire'), ('Permanent', 'Permanent')], max_length=9, null=True)),
                ('specialite', models.CharField(blank=True, max_length=300, verbose_name='Spécialité')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.personnel',),
        ),
        migrations.CreateModel(
            name='Tuteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('sexe', models.CharField(blank=True, choices=[('F', 'Féminin'), ('M', 'Masculin')], max_length=1)),
                ('adresse', models.CharField(blank=True, max_length=20, verbose_name='Adresse')),
                ('contact', models.CharField(max_length=25)),
                ('profession', models.CharField(blank=True, max_length=20, verbose_name='Profession')),
                ('type', models.CharField(blank=True, choices=[('pere', 'Père'), ('mere', 'Mère'), ('tuteur', 'Tuteur')], max_length=20)),
                ('etudiants', models.ManyToManyField(blank=True, to='main.etudiant', verbose_name='Étudiants')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.CharField(blank=True, max_length=14, primary_key=True, serialize=False)),
                ('libelle', models.CharField(choices=[('S1', 'Semestre1'), ('S2', 'Semestre2'), ('S3', 'Semestre3'), ('S4', 'Semestre4'), ('S5', 'Semestre5'), ('S6', 'Semestre6')], max_length=30)),
                ('credits', models.IntegerField(default=30)),
                ('semestreCourant', models.BooleanField(default=False, null=True, verbose_name='Semestre acutuelle')),
            ],
            options={
                'unique_together': {('libelle',)},
            },
        ),
        migrations.CreateModel(
            name='Salaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montantNet', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Montant Net')),
                ('montantBrut', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Montant Brut')),
                ('chargeSalariales', models.FloatField(verbose_name='Charges salariales')),
                ('chargePatronales', models.FloatField(verbose_name='Charges patronales')),
                ('bonification', models.DecimalField(decimal_places=2, max_digits=10)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.personnel', verbose_name='Personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anneescolaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anneeuniversitaire', verbose_name='Année universitaire')),
                ('parcours', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.parcours', verbose_name='Parcours')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.semestre', verbose_name='Semestre')),
                ('ue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ue', verbose_name='UE')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeurNote', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0.0)], verbose_name='note')),
                ('rattrapage', models.BooleanField(default=False)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.etudiant', verbose_name='Étudiant')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.evaluation', verbose_name='Evaluation')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codematiere', models.CharField(max_length=50, verbose_name='Code de la matière')),
                ('libelle', models.CharField(max_length=100)),
                ('coefficient', models.IntegerField(default='1', null=True, verbose_name='Coefficient')),
                ('minValue', models.FloatField(default='7', null=True, verbose_name='Valeur minimale')),
                ('heures', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('ue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ue')),
                ('enseignant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.enseignant', verbose_name='Enseignant')),
            ],
            options={
                'verbose_name_plural': 'Matières',
            },
        ),
        migrations.AddField(
            model_name='evaluation',
            name='etudiants',
            field=models.ManyToManyField(through='main.Note', to='main.etudiant', verbose_name='Étudiants'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.matiere', verbose_name='Matiere'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='semestre',
            field=models.ManyToManyField(to='main.semestre'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(choices=[('conge annuel', 'congé annuel'), ('conge de maternité', 'congé de maternité'), ('conge de paternite', 'congé de paternité'), (' autres', 'autres')], max_length=30)),
                ('dateHeureDepart', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de début')),
                ('dateHeureRetour', models.DateField(default=django.utils.timezone.now, verbose_name='Date de fin')),
                ('etat', models.CharField(choices=[('actif', 'Actif'), ('inactif', 'Inactif')], max_length=50)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.personnel', verbose_name='Personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.CharField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('libelle', models.CharField(max_length=100)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.matiere', verbose_name='Matiere')),
                ('ue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ue', verbose_name='UE')),
            ],
        ),
        migrations.CreateModel(
            name='Versement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('scolarite', 'Frais de scolarité'), ('inscription', 'Frais Inscription')], max_length=30)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Montant')),
                ('dateversement', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de versement')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.etudiant', verbose_name='Etudiant')),
                ('comptable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comptable', verbose_name='Comptable')),
            ],
        ),
        migrations.AddField(
            model_name='ue',
            name='enseignant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.enseignant', verbose_name='Enseignant'),
        ),
        migrations.AlterUniqueTogether(
            name='etudiant',
            unique_together={('nom', 'prenom', 'datenaissance', 'email')},
        ),
    ]
