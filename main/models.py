

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
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from datetime import datetime
import datetime

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
    role = models.CharField(max_length=50,default="User")
   

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
    anneeentree = models.IntegerField(default=datetime.date.today().year, blank=True, verbose_name="année entrée", null=False)
    anneebac1 = models.IntegerField(blank=True,verbose_name="Année d’obtention du BAC 1", null=True)
    anneebac2 = models.IntegerField(blank=True,verbose_name="Année d’obtention du BAC 2", null=True, default=datetime.date.today().year)
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
    passer_semestre_suivant =models.BooleanField(default=False, verbose_name="Passer au semestre suivant") 


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
            username = (self.prenom + self.nom).lower()
            year = date.today().year
            password = 'ifnti' + str(year) + '!'
            user = User.objects.create_user(username=username, password=password,email=self.email,last_name=self.nom,first_name=self.prenom,is_staff=False)
            
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

    def save(self):
        #print(self.id)
        if self.id == None:
            username = (self.prenom + self.nom).lower()
            year = date.today().year
            password = 'ifnti' + str(year) + '!'
            user = User.objects.create_user(username=username, password=password)
            self.user = user

        return super().save()
    
    def showId(self):
        return f'PER{self.id}'


class DirecteurDesEtudes(Personnel):
    actif = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            directeurs = DirecteurDesEtudes.objects.all()
            if directeurs:
                raise ValidationError("Il ne peut y avoir qu'un seul directeur des études.")
            
            username = (self.prenom[0] + self.nom).lower()
            password = "ifnti2023!"  # Définir le mot de passe souhaité
            user = User.objects.create_user(username=username, password=password, email=self.email, last_name=self.nom, first_name=self.prenom, is_staff=True)
            self.user = user

        if self.actif:
            # Désactiver les autres directeurs des études
            DirecteurDesEtudes.objects.exclude(pk=self.pk).update(actif=False)

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.actif:
            raise ValidationError("Le directeur des études actif ne peut pas être supprimé.")
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.prenom + " " + self.nom

    class Meta:
        verbose_name = "Directeur des études"
        verbose_name_plural = "Directeurs des études"
    


class Enseignant(Personnel):
    CHOIX_TYPE = (('Vacataire', 'Vacataire'), ('Permanent', 'Permanent'))
    type = models.CharField(null=True,blank=True,max_length=9, choices=CHOIX_TYPE)
    specialite =  models.CharField(max_length=300, verbose_name="Spécialité", blank=True)
    

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
            user =User.objects.create_user(username=username, password="ifnti2023!",email=self.email,last_name=self.nom,first_name=self.prenom,is_staff=True)
            self.user = user # On associe l'utilisateur à l'enseignant
            
        return super().save()

    def showId(self):
        return f'ENS{self.id}'

    def __str__(self):
        return "M. "+self.prenom + " " + self.nom



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

    def save(self):
        #print(self.id)
        if self.id == None:
            username = (self.prenom + self.nom).lower()
            year = date.today().year
            password = 'ifnti' + str(year) + '!'
            user = User.objects.create_user(username=username, password=password)
            self.user = user

        return super().save()



class Ue(models.Model):
    codeUE = models.CharField(max_length=50, verbose_name="Code de l'UE")
    libelle = models.CharField(max_length=100)
    TYPES = [("L", "Licence")]
    type = models.CharField(max_length=1, choices=TYPES, null=True)
    nbreCredits = models.IntegerField(verbose_name="Nombre de crédit")
    heures = models.DecimalField(blank=True, max_digits=4, decimal_places=1, validators=[MinValueValidator(1)])
    enseignant = models.ForeignKey('Enseignant', on_delete=models.CASCADE,verbose_name="Enseignant", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'UE'


    def __str__(self):
        return self.codeUE + " " + self.libelle


class Matiere(models.Model):
    codematiere = models.CharField(max_length=50, verbose_name="Code de la matière")
    libelle = models.CharField(max_length=100)
    coefficient = models.IntegerField(null=True,  verbose_name="Coefficient", default="1")
    minValue = models.FloatField(null=True,  verbose_name="Valeur minimale",  default="7")
    heures = models.DecimalField(blank=True, max_digits=4, decimal_places=1, validators=[MinValueValidator(1)], null=True) # Retirer plus tard le null
    enseignant = models.ForeignKey('Enseignant', on_delete=models.CASCADE,verbose_name="Enseignant",null=True, blank=True)
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
    
    def ponderation_restante(self):
        evaluations = Evaluation.objects.filter(matiere=self)
        ponderation_total = sum([evaluation.ponderation for evaluation in evaluations])
        return 100-ponderation_total


class Evaluation(models.Model):
    libelle = models.CharField(max_length=258, verbose_name="Nom")
    ponderation = models.IntegerField(default=1, verbose_name="Pondération (%)", validators=[MinValueValidator(1), MaxValueValidator(100)])
    date = models.DateField(verbose_name="Date")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, verbose_name='Matiere')
    etudiants = models.ManyToManyField(Etudiant, through='Note',verbose_name="Étudiants")


class Competence(models.Model):
    id = models.CharField(primary_key=True, blank=True, max_length=30)
    code = models.CharField(max_length=100)
    libelle = models.CharField(max_length=100)
    ue = models.ForeignKey('Ue', on_delete=models.CASCADE, verbose_name="UE")
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE, verbose_name="Matiere")


class Semestre(models.Model):
    id = models.CharField(primary_key=True, blank=True, max_length=14)
    CHOIX_SEMESTRE = [('S1', 'Semestre1'), ('S2', 'Semestre2'), ('S3', 'Semestre3'), ('S4', 'Semestre4'), ('S5', 'Semestre5'), ('S6', 'Semestre6')]
    libelle = models.CharField(max_length=30, choices=CHOIX_SEMESTRE)
    credits = models.IntegerField(default=30) 
    #semestreCourant = models.BooleanField(default=False, verbose_name="Semestre actuel", null=True)

    """clef Semestre"""

    def save(self):
        if not self.id: self.id = self.libelle +"-"+ str("A revoir avec malik")
        return super().save()

    def __str__(self):

        return self.libelle + " " + str("A revoir avec malik") + " " + str(self.semestreCourant)

    class Meta:
        unique_together = [["libelle"]]


class Domaine(models.Model):
    libelle = models.CharField(max_length=255, verbose_name="Libelle")
    description = models.TextField(max_length=500, verbose_name="description")
    def __str__(self):
        return self.libelle

class Seance(models.Model):
    intitule = models.CharField(max_length=200)
    date_et_heure_debut = models.DateTimeField()
    date_et_heure_fin = models.DateTimeField()
    description = models.TextField()
    auteur = models.ForeignKey(Etudiant, on_delete=models.CASCADE,related_name='seance_auteur',default='Anonyme')
    valider = models.BooleanField(default=False)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    eleves_presents = models.ManyToManyField(Etudiant,related_name='seances_presents')


    def __str__(self):
        return self.intitule
        



class Parcours(models.Model):
    libelle = models.CharField(max_length=255, verbose_name="Libelle")
    domaine = models.ForeignKey(Domaine, on_delete = models.CASCADE, verbose_name="Domaine", null=True)
    description = models.TextField(max_length=500, verbose_name="description")
    def __str__(self):
        return self.libelle


class AnneeUniversitaire(models.Model):
    anneeUniv = models.CharField(max_length=300, verbose_name="Année universitaire")
    #anneeUnivCourante = models.BooleanField(default=False, verbose_name="Année universitaire acutuelle", null=True)
    
    def __str__(self):
        return str(self.anneeUniv)


class Programme(models.Model):
    parcours = models.ForeignKey(Parcours, on_delete=models.CASCADE, verbose_name="Parcours", null=True, blank=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, verbose_name="Semestre")
    ue = models.ForeignKey(Ue, on_delete=models.CASCADE, verbose_name="UE")
    anneescolaire = models.ForeignKey(AnneeUniversitaire, on_delete=models.CASCADE, verbose_name="Année universitaire")

class Note(models.Model):
    """
    Ce modèle représente la note d'un étudiant dans un semestre et une matière donnée.

    Attributes:
        valeurNote (decimal): La valeur de la note.
        etudiant (Etudiant): L'étudiant à qui cette note appartient.
        matiere (Matiere): La matière dans laquelle l'étudiant a eu cette note. 
    
    Methods:
        __str__() -> str: Renvoie une représentation en chaîne de caractères de l'objet Note.
    """
    valeurNote = models.DecimalField(default=0.0, blank=False,max_digits=5, decimal_places=2, verbose_name="note", validators=[MaxValueValidator(20), MinValueValidator(0.0)])
    rattrapage = models.BooleanField(default=False)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE,verbose_name="Étudiant")
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, verbose_name="Evaluation")

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères de l'objet Note.

        Returns:
            str: La représentation en chaîne de caractères de l'objet Note.
        """
        return str(self.id) + " " + str(self.evaluation) + " " + str(self.valeurNote)


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
 


class Paiement(models.Model):
    TYPE_CHOISE = [
        ('scolarite','Frais de scolarité'),
    ]
    type = models.CharField(max_length=30, choices=TYPE_CHOISE)
    montant = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name="Montant versé")
    fraisconcours = models.IntegerField(default=10000, verbose_name="Frais de concours")
    fraisinscription = models.IntegerField(default=30000, verbose_name="Frais de concours")
    dateversement = models.DateField(default=timezone.now, verbose_name="Date de versement")
    nombreTranche = models.IntegerField(verbose_name="Nombre de tranche")
    debit = models.IntegerField(default=590000, verbose_name="Débit")
    credit = models.IntegerField(default=0, verbose_name="Crédit")
    numerobordereau = models.CharField(max_length=30, verbose_name="Numéro de bordereau")
    bordereau = models.FileField(upload_to='bordereau/', null=True, verbose_name="Bordereau de paiement")
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE, verbose_name="Etudiant") 
    comptable = models.ForeignKey('Comptable', on_delete=models.CASCADE, verbose_name="Comptable")

    def save(self, *args, **kwargs):
        if self.credit < 590000 and self.debit > 0:
            difference = min(self.montant, 590000 - self.credit)
            self.credit += difference
            self.debit -= difference
            if self.credit == 590000 and self.debit == 0:
                self.nombreTranche += 1
        super(Paiement, self).save(*args, **kwargs)

class Information(models.Model):
    TYPE_CHOISE = [
        ('Premier','Niveau 1'),
        ('Deuxième','Niveau 2'),
        ('Troisième','Niveau 3'),
    ]
    nomDirecteur = models.CharField(max_length=100, verbose_name="Nom du directeur")
    prenomDirecteur = models.CharField(max_length=100, verbose_name="Prénom du directeur")
    nomEnseignant = models.CharField(max_length=100, verbose_name="Nom de l'enseignant")
    prenomEnseignant = models.CharField(max_length=100, verbose_name="Prénom de l'enseignant")
    numeroSecurite = models.IntegerField(verbose_name="Numéro de sécurité sociale")
    discipline = models.CharField(max_length=100, verbose_name="Discipline")
    niveau = models.CharField(max_length=100, choices=TYPE_CHOISE, verbose_name="Niveau")
    dateDebut = models.DateField(verbose_name="Date de début")
    dateFin = models.DateField(verbose_name="Date de fin")
    duree = models.CharField(max_length=100, verbose_name="Durée")

    def __str__(self):
        return str(self.nomDirecteur) + " " + str(self.nomEnseignant) + " " + str(self.numeroSecurite) + " " + str(self.discipline) + " " + str(self.niveau) + " " + str(self.dateDebut) + " " + str(self.dateFin) + " " + str(self.duree)


class FicheDePaie(models.Model):
    TYPE_CHOISE = [
        ('semestre1','S1'),
        ('semestre2','S2'),
    ]
    TYPE_CHOISE1 = [
        ('semestre3','S3'),
        ('semestre4','S4'),
    ]
    TYPE_CHOISE2 = [
        ('semestre5','S5'),
        ('semestre6','S6'),
    ]

    bp = models.IntegerField(verbose_name="B.P" , default=40)
    telephone = models.IntegerField(verbose_name="Téléphone", default=90918141)
    dateDebut = models.DateField(verbose_name="Date de début")
    dateFin = models.DateField(verbose_name="Date de fin")
    matiere = models.CharField(max_length=100, verbose_name="Matière")
    enseignant = models.ForeignKey('Enseignant', on_delete=models.CASCADE, verbose_name="Enseignant")
    nombreHeure = models.IntegerField(verbose_name="Nombre d'heure")
    prixUnitaire = models.IntegerField(verbose_name="Prix unitaire", default=2000)
    montantTotal = models.IntegerField(verbose_name="montantTotal", default=0)
    montantAvance = models.IntegerField(verbose_name="Montant avance")
    montantAPayer = models.IntegerField(verbose_name="Montant à payer")
    montantEnLettre = models.CharField(max_length=100, verbose_name="Montant en lettre")
    numero = models.IntegerField(verbose_name="Numéro")
    niveau1 = models.CharField(max_length=30, choices=TYPE_CHOISE)
    niveau2 = models.CharField(max_length=30, choices=TYPE_CHOISE1)
    niveau3 = models.CharField(max_length=30, choices=TYPE_CHOISE2)
    heureL1 = models.IntegerField(verbose_name="Heure L1")
    heureL2 = models.IntegerField(verbose_name="Heure L2")
    heureL3 = models.IntegerField(verbose_name="Heure L3")
    montantL1 = models.IntegerField(verbose_name="Montant L1")
    montantL2 = models.IntegerField(verbose_name="Montant L2")
    montantL3 = models.IntegerField(verbose_name="Montant L3")
    
    def __str__(self):
        return str(self.bp) + " " + str(self.telephone) + " " + str(self.dateDebut) + " " + str(self.dateFin) + " " + str(self.matiere) + " " + str(self.enseignant) + " " + str(self.nombreHeure) + " " + str(self.prixUnitaire) + " " + str(self.montantTotal) + " " + str(self.montantAvance) + " " + str(self.montantAPayer) + " " + str(self.montantEnLettre) + " " + str(self.numero) + " " + str(self.niveau1) + " " + str(self.niveau2) + " " + str(self.niveau3) + " " + str(self.heureL1) + " " + str(self.heureL2) + " " + str(self.heureL3) + " " + str(self.montantL1) + " " + str(self.montantL1) + " " + str(self.montantL2) + " " + str(self.montantL3)