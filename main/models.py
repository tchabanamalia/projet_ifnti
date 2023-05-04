
from django.db import models
from django.conf import settings
from tabnanny import verbose
from django.contrib.auth.models import User 
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Utilisateur(models.Model):  
    SEXE_CHOISE = [
        ('F','Feminin'),
        ('M','Masculin')
    ]
    nom=models.CharField(max_length=50) 
    prenom = models.CharField(max_length=50, verbose_name="Prénom") 
    sexe = models.CharField(max_length=1, choices=SEXE_CHOISE)
    datenaissance = models.DateField(blank=True,verbose_name="date de naissance",null=True, validators=[MaxValueValidator(limit_value=date(2006, 1,1), message="L'année de naissance doit être inférieure à 2006")])
    lieunaissance = models.CharField(blank=True,max_length=20, verbose_name="lieu de naissance")
    contact = models.CharField(max_length=25)
    email=models.CharField(max_length=50, null=True)
    adresse=models.CharField(max_length=50)
    prefecture=models.CharField(max_length=50, null=True, verbose_name="Préfecture", default='tchaoudjo',blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Actif")    
    carte_identity = models.CharField(max_length=50, null=True,  verbose_name="Carte d'identité")
    nationalite = models.CharField(max_length=30, default='Togolaise', verbose_name='Nationalté',blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


    def __str__(self):
        return str(self.nom) + ' ' + str(self.prenom) 
    
    def suspendre(self):
        self.is_active = False
        self.save()


    def reactiver(self):
        self.is_active = True
        self.save()



class Etudiant(Utilisateur):
    id = models.CharField(primary_key=True, blank=True, max_length=12)
    CHOIX_SERIE = [('A', 'A'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F1', 'F1'), ('F2', 'F2'), ('F3', 'F3'),
                   ('F4', 'F4'), ('G2', 'G2')]
    seriebac1 = models.CharField(blank=True,max_length=2, choices=CHOIX_SERIE, verbose_name="Série bac 1", null=True)
    seriebac2 = models.CharField(blank=True,max_length=2, choices=CHOIX_SERIE, verbose_name="Série bac 2", null=True)

    anneeentree = models.IntegerField(blank=True,verbose_name="année entrée", null=False)

    anneebac1 = models.IntegerField(blank=True,verbose_name="Année d’obtention du BAC 1", null=True)
    anneebac2 = models.IntegerField(blank=True,verbose_name="Année d’obtention du BAC 2", null=True)

    etablissementSeconde = models.CharField(max_length=300, verbose_name="Nom d'établissement seconde", null=True, blank=True)
    francaisSeconde = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note de français Seconde", default="0")
    anglaisSeconde = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note d'anglais Seconde", default="0")
    mathematiqueSeconde = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note de mathématique Seconde", default="0")

    etablissementPremiere = models.CharField(max_length=300, verbose_name="Nom d'établissement Première", null=True, blank=True)
    francaisPremiere = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note de français Première", default="0")
    anglaisPremiere = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note d'anglais Première", default="0")
    mathematiquePremiere = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note de mathématique Première", default="0")

    etablissementTerminale = models.CharField(max_length=300, verbose_name="Nom d'établissement Terminale", null=True, blank=True)
    francaisTerminale = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note de français Terminale", default="0")
    anglaisTerminale = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note d'anglais Terminale", default="0")
    mathematiqueTerminale = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Note de mathématique Terminale", default="0")

    semestre = models.ManyToManyField('Semestre')



    class Meta:
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants" 
        unique_together = [["nom", "prenom", "datenaissance", "email"]]


    """ Cléf de l'étudiant"""

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            list_etudiants = Etudiant.objects.filter(anneeentree=self.anneeentree)
            if list_etudiants:
                n = 1
                rang = "0" + str(len(list_etudiants) + n) if len(
                    list_etudiants) + n < 10 else str(
                    len(list_etudiants) + n)
                val_id = self.nom[0] + self.prenom[0] + str(self.anneeentree) + rang
                for i in [etud.id for etud in list_etudiants]:
                    if val_id == i:
                        n = n + 1
                        rang = "0" + str(len(list_etudiants) + n) if len(
                            list_etudiants + n) < 10 else str(
                            len(list_etudiants) + n)
                        val_id = self.nom[0] + self.prenom[0] + str(self.anneeentree) + rang
                self.id = val_id
            else:
                self.id = self.nom[0] + self.prenom[0] + str(self.anneeentree) + "0" + str(1)
            # Création de l'utilisateur associé à l'instance de l'étudiant
            username = (self.prenom[0] + self.nom).lower()
            year = datetime.datetime.now().year
            password = 'ifnti' + str(year) + '!'
            user = User.objects.create_user(username=username, password=password)

            self.user = user # association de l'utilisateur à l'instance de l'étudiant
        return super().save()

    def __str__(self):
        return self.id + " " + self.nom + " " + self.prenom



class Personnel(Utilisateur):
    id = models.CharField(primary_key=True, blank=True, max_length=12)  
    salaireBrut = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name="Salaire Brut")
    dernierdiplome = models.ImageField(null=True, blank=True, verbose_name="Dernier diplome")
    nbreJrsCongesRestant = models.IntegerField(verbose_name="Nonbre de jours de congé restant")
    nbreJrsConsomme = models.IntegerField(verbose_name="Nonbre de jours consommé")



class Enseignant(Personnel):
    CHOIX_TYPE = (('Vacataire', 'Vacataire'), ('Permanent', 'Permanent'))
    type = models.CharField(null=True,blank=True,max_length=9, choices=CHOIX_TYPE)
    specialite =  models.CharField(max_length=300, verbose_name="Spécialité", blank=True)
   

    """clef enseignant"""

    def save(self):
        if not self.id:
            enseignants = Enseignant.objects.all()
            if enseignants:
                rang_ens = int(enseignants.last().id.replace("ENS", ""))
                self.id = "ENS" + str(rang_ens + 1)
            else:
                self.id = "ENS" + str(1)
            # Création de l'utilisateur associé à l'instance de l'enseignant
            username = (self.prenom[0] + self.nom).lower()
            user = User.objects.create_user(username=username, password="ifnti2023!")
            self.user = user # On associe l'utilisateur à l'enseignant
        return super().save()

    def __str__(self):
        return self.prenom + " " + self.nom




class Comptable(Personnel):
    pass



class Tuteur(models.Model):
    CHOIX_SEX = [
        ("F", "Féminin"),
        ("M", "Masculin")
    ]
    CHOIX_TYPE = [
        ("pere", "Père"),
        ("mere", "Mère"),
        ("tuteur", "Tuteur"),
    ]
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    sexe = models.CharField(blank=True,max_length=1, choices=CHOIX_SEX)
    adresse = models.CharField(blank=True,max_length=20, verbose_name="Adresse")
    contact = models.CharField(max_length=25)
    profession = models.CharField(blank=True,max_length=20, verbose_name="Profession")
    type = models.CharField(blank=True,max_length=20, choices=CHOIX_TYPE)
    etudiants = models.ManyToManyField("Etudiant", verbose_name="Étudiants", blank=True)
   



class Ue(models.Model):
    codeUE = models.CharField(max_length=50, verbose_name="Code de l'UE")
    libelle = models.CharField(max_length=100)
    nbreCredits = models.IntegerField(verbose_name="Nombre de crédit")
    heures = models.DecimalField(blank=True, max_digits=4, decimal_places=1)
    enseignant = models.ForeignKey('Enseignant', on_delete=models.CASCADE,verbose_name="Enseignant",null=True,blank=True)
    semestre = models.ForeignKey('Semestre', on_delete=models.CASCADE, verbose_name="Semestre")
 
    class Meta:
        verbose_name_plural = 'UE'


    def __str__(self):
        return self.codeUE + " " + self.libelle




class Matiere(models.Model):
    codematiere = models.CharField(max_length=50, verbose_name="Code de la matière")
    libelle = models.CharField(max_length=100)
    coefficient = models.IntegerField(null=True,  verbose_name="Coefficient", default="1")    
    minValue = models.FloatField(null=True,  verbose_name="Valeur minimale")
    enseignant = models.ForeignKey('Enseignant', on_delete=models.CASCADE)
    ue = models.ForeignKey('Ue', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name="Actif")


    def __str__(self):
        return self.codematiere + " " + self.libelle    

    class Meta:
        verbose_name_plural = "Matières"

    def suspendre(self):
        self.is_active = False
        self.save()

    def reactiver(self):
        self.is_active = True
        self.save()



class Competence(models.Model):
    id = models.CharField(primary_key=True, blank=True, max_length=30)
    code = models.CharField(max_length=100)
    libelle = models.CharField(max_length=100)
    ue = models.ForeignKey('Ue', on_delete=models.CASCADE, verbose_name="UE")
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE, verbose_name="Matiere")

   



class MaquetteGenerique(models.Model):
    pass



class Semestre(models.Model):
    id = models.CharField(primary_key=True, blank=True, max_length=14)
    CHOIX_SEMESTRE = [('S1', 'Semestre1'), ('S2', 'Semestre3'), ('S3', 'Semestre3'), ('S4', 'Semestre4'), ('S5', 'Semestre5'), ('S6', 'Semestre6')]
    libelle = models.CharField(max_length=30, choices=CHOIX_SEMESTRE)
    anneescolaire = models.ForeignKey('AnneeUniversitaire', on_delete=models.CASCADE, verbose_name="Année universitaire")
    credits = models.IntegerField(default=30) 
   
    """clef Semestre"""

    def save(self):
        if not self.id: self.id = self.libelle +"-"+ str(self.anneescolaire)
        return super().save()

    def __str__(self):
        return self.libelle + " " + str(self.anneescolaire)

    class Meta:
        unique_together = [["anneescolaire", "libelle"]]





class AnneeUniversitaire(models.Model):
    anneeUniv = models.CharField(max_length=300, verbose_name="Année universitaire")

    def __str__(self):
        return str(self.anneeUniv)



class Note(models.Model):
    """
    Ce modèle représente la note d'un étudiant dans un semestre et une matière donnée.

    Attributes:
        valeurNote (decimal): La valeur de la note.
        etudiant (Etudiant): L'étudiant à qui cette note appartient.
        semestre (Semestre): Le semestre au cours duquel l'étudiant a eu cette note.
        matiere (Matiere): La matière dans laquelle l'étudiant a eu cette note. 
    
    Methods:
        __str__() -> str: Renvoie une représentation en chaîne de caractères de l'objet Note.

    """
    valeurNote = models.DecimalField(null=True, max_digits=4, decimal_places=2, verbose_name="note", validators=[MaxValueValidator(20), MinValueValidator(-0.01)])
    rattrapage = models.BooleanField(default=False)
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE,verbose_name="Étudiant")
    #semestre = models.ForeignKey('Semestre', on_delete=models.CASCADE, verbose_name="Semestre")
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE, verbose_name="Matiere")


    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères de l'objet Note.

        Returns:
            str: La représentation en chaîne de caractères de l'objet Note.
        """
        return str(self.etudiant) + " " + str(self.matiere) + " " + str(self.valeurNote)




class Salaire(models.Model):
    montantNet = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant Net")
    montantBrut = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name="Montant Brut")
    chargeSalariales = models.FloatField(verbose_name="Charges salariales")
    chargePatronales = models.FloatField(verbose_name="Charges patronales")
    bonification = models.DecimalField(max_digits=10, decimal_places=2)
    personnel = models.ForeignKey('Personnel', on_delete=models.CASCADE, verbose_name="Personnel") 



class Conge(models.Model):
    ETAT_CHOISE = [
        ('actif','Actif'),
        ('inactif','Inactif')
    ]


    NATURE_CHOISE = [
        ('conge annuel','congé annuel'),
        ('conge de maternité','congé de maternité'),
        ('conge de paternite','congé de paternité'),
        (' autres','autres'),      
    ]

    nature = models.CharField(max_length=30, choices=NATURE_CHOISE)
    dateHeureDepart = models.DateTimeField(default=timezone.now, verbose_name="Date de début")
    dateHeureRetour = models.DateField(default=timezone.now, verbose_name="Date de fin")
    etat = models.CharField(max_length=50, choices=ETAT_CHOISE)
    personnel = models.ForeignKey('Personnel', on_delete=models.CASCADE, verbose_name="Personnel") 



class Versement(models.Model):
    TYPE_CHOISE = [
        ('scolarite','Frais de scolarité'),
        ('inscription','Frais Inscription')
    ]
    type = models.CharField(max_length=30, choices=TYPE_CHOISE)
    montant = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name="Montant")
    dateversement = models.DateTimeField(default=timezone.now, verbose_name="Date de versement")
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE, verbose_name="Etudiant") 
    comptable = models.ForeignKey('Comptable', on_delete=models.CASCADE, verbose_name="Comptable") 
