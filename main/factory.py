import factory
import factory.fuzzy
from django.utils import timezone
from .models import AnneeUniversitaire, Etudiant, MaquetteGenerique, Semestre

FAKER = factory.faker.faker.Faker()

# class AnneeUniversitaireFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = AnneeUniversitaire
#     anneeUniv = factory.Faker('year-year')

"""
from main.factory import SemestreFactory
force_insert=False
semestre = SemestreFactory()
x = SemestreFactory.create_batch(3)
"""



class SemestreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Semestre
    libelle = factory.fuzzy.FuzzyChoice(['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
    anneescolaire = AnneeUniversitaire.objects.get_or_create(anneeUniv="2022-2023")[0]
    credits = factory.Faker('pydecimal', left_digits=2, positive=True)
    maquetteGenerique = MaquetteGenerique.objects.get_or_create()[0]
    def save(self, *args, **kwargs):
        # supprimer l'argument force_insert
        super(Semestre, self).save(*args, **kwargs)

""""
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'path.to.User'

    # ...les champs de votre modèle User

class EtudiantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Etudiant

    nom = factory.Faker('last_name')
    prenom = factory.Faker('first_name')
    sexe = factory.fuzzy.FuzzyChoice(['M', 'F'])
    datenaissance = factory.Faker('date_of_birth', minimum_age=16, maximum_age=30)
    lieunaissance = factory.Faker('city')
    contact = factory.Faker('phone_number')
    email = factory.Faker('email')
    adresse = factory.Faker('address')
    prefecture = factory.Faker('city')
    etat = factory.fuzzy.FuzzyChoice(['actif', 'inactif'])
    carte_identity = factory.Faker('ssn')
    nationalite = 'Togolaise'
    user = factory.SubFactory('path.to.UserFactory')
    seriebac1 = factory.fuzzy.FuzzyChoice(['A', 'C', 'D', 'E', 'F1', 'F2', 'F3', 'F4', 'G2'])
    seriebac2 = factory.fuzzy.FuzzyChoice(['A', 'C', 'D', 'E', 'F1', 'F2', 'F3', 'F4', 'G2'])
    anneeentree = factory.fuzzy.FuzzyInteger(2010, 2020)
    anneebac1 = factory.fuzzy.FuzzyInteger(2005, 2015)
    anneebac2 = factory.fuzzy.FuzzyInteger(2005, 2015)
    etablissementSeconde = factory.Faker('company')
    francaisSeconde = factory.fuzzy.FuzzyDecimal(0, 20, 2)
    anglaisSeconde = factory.fuzzy.FuzzyDecimal(0, 20, 2)
    mathematiqueSeconde = factory.fuzzy.FuzzyDecimal(0, 20, 2)
    etablissementPremiere = factory.Faker('company')
    francaisPremiere = factory.fuzzy.FuzzyDecimal(0, 20, 2)
    anglaisPremiere = factory.fuzzy.FuzzyDecimal(0, 20, 2)
    mathematiquePremiere = factory.fuzzy.FuzzyDecimal(0, 20, 2)
    etablissementTerminale = factory.Faker('company')
    francaisTerminale = factory.fuzzy.FuzzyDecimal(0, 20, 2)
    anglaisTerminale = factory.fuzzy.FuzzyDecimal(0, 20, 2)
    mathematiqueTerminale = factory.fuzzy.FuzzyDecimal(0, 20, 2)

"""
