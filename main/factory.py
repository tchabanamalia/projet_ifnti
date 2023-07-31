import random
from faker import Faker
from main.models import Etudiant, Personnel, Enseignant, Comptable, Programme, Tuteur, Ue, Matiere, Evaluation, Competence, Semestre, Domaine, Parcours, AnneeUniversitaire, Note
from django.contrib.auth.models import User 
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
user = User.objects.filter(username="amk2048")[0]
for us in User.objects.all():
    if us != user : us.delete()
print("Drop all object .....")
Personnel.objects.all().delete()
print("Drop all object .....")
Enseignant.objects.all().delete()
print("Drop all object .....")
Etudiant.objects.all().delete()
print("Drop all object .....")
Comptable.objects.all().delete()
print("Drop all object .....")
Tuteur.objects.all().delete()
print("Drop all object .....")
Ue.objects.all().delete()
print("Drop all object .....")
Matiere.objects.all().delete()
print("Drop all object .....")
Evaluation.objects.all().delete()
print("Drop all object .....")
Competence.objects.all().delete()
print("Drop all object .....")
Semestre.objects.all().delete()
print("Drop all object .....")
Domaine.objects.all().delete()
print("Drop all object .....")
Parcours.objects.all().delete()
print("Drop all object .....")
Note.objects.all().delete()
print("Drop all object .....")
AnneeUniversitaire.objects.all().delete()
print("Drop all object .....")

fake = Faker()

# Création de 10 objets Personnel fictifs
for _ in range(10):
    # Génération des données aléatoires
    nom = fake.last_name()
    prenom = fake.first_name()
    sexe = random.choice(['F', 'M'])
    datenaissance = fake.date_of_birth(minimum_age=18, maximum_age=60)
    lieunaissance = fake.city()
    contact = fake.phone_number()
    email = fake.email()
    adresse = fake.address()
    prefecture = fake.city()
    carte_identity = fake.random_number(digits=8)
    nationalite = fake.country()
    salaireBrut = fake.pydecimal(left_digits=5, right_digits=2, positive=True)
    nbreJrsCongesRestant = random.randint(0, 30)

    # Création de l'objet Personnel
    personnel = Personnel(
        nom=nom,
        prenom=prenom,
        sexe=sexe,
        datenaissance=datenaissance,
        lieunaissance=lieunaissance,
        contact=contact,
        email=email,
        adresse=adresse,
        prefecture=prefecture,
        carte_identity=carte_identity,
        nationalite=nationalite,
        salaireBrut=salaireBrut,
        nbreJrsCongesRestant=nbreJrsCongesRestant,
        nbreJrsConsomme=0
    )
    personnel.save()

    # Génération d'une image de diplôme aléatoire
    diplome_data = fake.image()
    diplome_temp = NamedTemporaryFile(delete=True)
    diplome_temp.write(diplome_data)
    diplome_temp.flush()
    personnel.dernierdiplome.save(f"diplome_{personnel.id}.png", File(diplome_temp))

    # Affichage des informations générées
    print(f"Personnel créé : {personnel}")

for _ in range(10):
    etudiant = Etudiant(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        sexe=random.choice(['F', 'M']),
        datenaissance=fake.date_of_birth(minimum_age=18, maximum_age=30),
        lieunaissance=fake.city(),
        contact=fake.phone_number(),
        email=fake.email(),
        adresse=fake.address(),
        prefecture=fake.city(),
        carte_identity=fake.random_number(digits=10),
        nationalite='Togolaise',
        anneeentree = fake.random_int(min=2010, max=2023),
        seriebac1 = random.choice(['A', 'C', 'D', 'E', 'F1', 'F2', 'F3', 'F4', 'G2']),
        seriebac2 = random.choice(['A', 'C', 'D', 'E', 'F1', 'F2', 'F3', 'F4', 'G2']),
        anneebac1 = fake.random_int(min=2000, max=2022),
        anneebac2 = fake.random_int(min=2000, max=2022),
        etablissementSeconde = fake.company(),
        francaisSeconde = round(random.uniform(10, 20), 2),
        anglaisSeconde = round(random.uniform(10, 20), 2),
        mathematiqueSeconde = round(random.uniform(10, 20), 2),
        etablissementPremiere = fake.company(),
        francaisPremiere = round(random.uniform(10, 20), 2),
        anglaisPremiere = round(random.uniform(10, 20), 2),
        mathematiquePremiere = round(random.uniform(10, 20), 2),
        etablissementTerminale = fake.company(),
        francaisTerminale = round(random.uniform(10, 20), 2),
        anglaisTerminale = round(random.uniform(10, 20), 2),
        mathematiqueTerminale = round(random.uniform(10, 20), 2)
    )
    etudiant.save()
    print(f"Etudiant créé : {etudiant}")

# Génération des fausses instances pour le modèle Enseignant
personnels = Personnel.objects.all()
for _ in range(10):
    nom = fake.last_name()
    prenom = fake.first_name()
    username = f"{prenom.lower()}.{nom.lower()}"
    password = fake.password()
    enseignant = Enseignant(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        sexe=random.choice(['F', 'M']),
        datenaissance=fake.date_of_birth(minimum_age=25, maximum_age=60),
        lieunaissance=fake.city(),
        contact=fake.phone_number(),
        email=fake.email(),
        adresse=fake.address(),
        prefecture=fake.city(),
        carte_identity=fake.random_number(digits=10),
        nationalite='Togolaise',
        salaireBrut=random.uniform(1000, 5000),
        dernierdiplome=None,
        nbreJrsCongesRestant=random.randint(0, 30),
        nbreJrsConsomme=random.randint(0, 30),
        specialite=fake.job(),
    )
    enseignant.save()
    print(f"Enseignant créé : {enseignant}")


# Génération des fausses instances pour le modèle Comptable
for _ in range(10):
    comptable = Comptable(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        sexe=random.choice(['F', 'M']),
        datenaissance=fake.date_of_birth(minimum_age=25, maximum_age=60),
        lieunaissance=fake.city(),
        contact=fake.phone_number(),
        email=fake.email(),
        adresse=fake.address(),
        prefecture=fake.city(),
        carte_identity=fake.random_number(digits=10),
        nationalite='Togolaise',
        salaireBrut=random.uniform(1000, 5000),
        dernierdiplome=None,
        nbreJrsCongesRestant=random.randint(0, 30),
        nbreJrsConsomme=random.randint(0, 30),
    )
    comptable.save()
    print(f"Comptable créé : {comptable}")

# Génération des fausses instances pour le modèle Tuteur
etudiants = Etudiant.objects.all()
for _ in range(10):
    tuteur = Tuteur(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        sexe=random.choice(['F', 'M']),
        type=random.choice(["Père", "Mère", "Tuteur"]),
        contact=fake.phone_number(),
        profession=fake.job(),
    )
    tuteur.save()
    print(f"Tuteur créé : {tuteur}")

# Génération des fausses instances pour le modèle Domaine
domaine = Domaine(
    libelle="Siences et technologie",
    description=fake.sentence()
)
domaine.save()
print(f"Domaine créé : {domaine}")

# Génération des fausses instances pour le modèle Parcours
domaines = Domaine.objects.all()

parcours = Parcours(
    #code=fake.unique.random_number(digits=3),
    libelle="Licence en génie logiciel",
    domaine=domaine,
    description=fake.sentence()
)
parcours.save()
print(f"Parcours créé : {parcours}")

# Génération des fausses instances pour le modèle Ue
for _ in range(5):
    # Génération des données aléatoires
    codeUE = str(fake.random_int(min=1000, max=9999))
    libelle = fake.catch_phrase()
    nbreCredits = random.randint(1, 10)
    heures = round(random.uniform(10, 100), 1)
    enseignant = random.choice(Enseignant.objects.all())

    # Création de l'objet Ue
    ue = Ue.objects.create(
        codeUE=codeUE,
        libelle=libelle,
        nbreCredits=nbreCredits,
        heures=heures,
        enseignant=enseignant,
    )
    print(f"Ue créé : {ue}")


# Génération des fausses instances pour le modèle Matiere
ues = Ue.objects.all()
for _ in range(20):
    matiere = Matiere(
        codematiere=str(fake.unique.random_number(digits=5)),
        libelle=fake.word(),
        coefficient=random.uniform(1, 3),
        heures=round(random.uniform(10, 100), 1),
        ue=random.choice(ues),
        minValue = fake.random_int(min=5, max=12),
        enseignant = random.choice(Enseignant.objects.all()),
        is_active = True
    )
    matiere.save()
    print(f"Matiere créé : {matiere}")


# Génération des fausses instances pour le modèle AnneeUniversitaire
current = False
for _ in range(10):
    if _ == 9:
        current = True
    annee_universitaire = AnneeUniversitaire(
        anneeUniv=fake.date_between(start_date='-2y', end_date='+1y'),
        anneeUnivCourante=current
    )
    annee_universitaire.save()
    print(f"AnneeUniversitaire créé : {annee_universitaire}")

semestres = ["Semestre1", "Semestre3", "Semestre5"]
for s in semestres:
    semestre = Semestre(
    libelle=s,
    credits=30,
    semestreCourant=True,
    )
    semestre.save()
    print(f"Semestre créé : {semestre}")

# Génération des fausses instances pour le modèle Note
etudiants = Etudiant.objects.all()
annees_universitaire = random.choice(AnneeUniversitaire.objects.all())

for _ in range(10):
    programme = Programme(
        parcours=Parcours.objects.all()[0],
        ue=random.choice(Ue.objects.all()),
        semestre=Semestre.objects.all()[0],
        anneescolaire=annees_universitaire,
    )
    programme.save()
    print(f"Programme créé : {programme}")

"""for _ in range(10):
    note = Note(
        valeurNote=random.uniform(0, 20),
        etudiant=random.choice(etudiants),
        evaluation=random.choice(Evaluation.objects.all()),
        rattrapage = False
    )
    note.save()
    print(f"Note créé : {note}")
"""

"""
# Création de 10 objets Evaluation fictifs
for _ in range(10):
    # Génération des données aléatoires
    libelle = fake.catch_phrase()
    ponderation = random.randint(1, 100)
    date = fake.date_between(start_date='-1y', end_date='today')
    matiere = random.choice(Matiere.objects.all())

    # Création de l'objet Evaluation
    evaluation = Evaluation.objects.create(
        libelle=libelle,
        ponderation=ponderation,
        date=date,
        matiere=matiere
    )

    # Ajout d'étudiants et de notes fictives
    etudiants = Etudiant.objects.all()
    for etudiant in etudiants:
        note = random.uniform(0, 20)
        Note.objects.create(evaluation=evaluation, etudiant=etudiant, note=note)

    # Affichage des informations générées


# Génération des fausses instances pour le modèle Competence
for _ in range(10):
    competence = Competence(
        libelle=fake.word(),
        description=fake.sentence()
    )
    competence.save()
    print(f"Competence créé : {competence}")

# Génération des fausses instances pour le modèle MaquetteGenerique
semestres = Semestre.objects.all()
matieres = Matiere.objects.all()
competences = Competence.objects.all()
for _ in range(10):
    maquette_generique = MaquetteGenerique(
        code=fake.unique.random_number(digits=5),
        libelle=fake.word(),
        semestre=random.choice(semestres),
        matiere=random.choice(matieres),
        competence=random.choice(competences)
    )
    maquette_generique.save()
    print(f"MaquetteGenerique créé : {maquette_generique}")

# Génération des fausses instances pour le modèle Semestre
for _ in range(10):
    semestre = Semestre(
        code=fake.unique.random_number(digits=2),
        libelle=fake.word()
    )
    semestre.save()
    print(f"Semestre créé : {semestre}")
"""
""" 
import main.factory
"""
