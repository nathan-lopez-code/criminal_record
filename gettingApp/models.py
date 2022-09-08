from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField

def changname(instance, filename):
    filename, extension = filename.split('.')
    name_ = instance.name + instance.postnom
    return 'profile/%s.%s' % (name_, extension)


class CriminalProfil(models.Model):
    """ profile du criminel """

    # constants
    GENDER = (
        ('M', 'Homme'),
        ('F', 'Femme')
    )

    ETAT_CIVIL = (
        ("marié", "marié"),
        ("célibataire", "célibataire"),
        ('divorcé', 'divorcé'),
        ('veuve ou veuf', 'veuve ou veuf'),
    )

    # informations personnels
    name = models.CharField(max_length=50)
    postnom = models.CharField(verbose_name="post nom", max_length=50)
    prenom = models.CharField(verbose_name="prenom", max_length=50, blank=True, null=True)
    genre = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)

    # lieu et date de naissance
    lieu = models.CharField(verbose_name='lieu de naissance', max_length=80, blank=True, null=True)
    date = models.DateField(verbose_name='date de naissance', null=True)

    # photos
    photo = models.ImageField(upload_to=changname, null=True)

    # origine
    nom_pere = models.CharField(max_length=100, verbose_name="nom du père", blank=True, null=True)
    nom_mere = models.CharField(max_length=100, verbose_name="nom de la mère", blank=True, null=True)
    
    # autre informations

    adresse = models.CharField(max_length=100, default="30 av. lufira v.Paris", blank=True, null=True)
    etatcivile = models.CharField(max_length=30, verbose_name="Etat civil", choices=ETAT_CIVIL, blank=True, null=True)
    nationalite = models.CharField(max_length=40, default="nationalité", blank=True, null=True)
    profession = models.CharField(max_length=100, default="footbaleur", blank=True, null=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('settingApp:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} : {}".format(self.name, self.postnom)

    class Meta:
        ordering = ['name']


class Crime(models.Model):

    # constantes
    TYPE_DELIT = (
        ('contravention', 'contravention'),
        ('delit', 'delit'),
        ('crime', 'crime'),
    )
    TYPE_DE_PEINE = (
        ('privation de liberté(emprisonnement)', 'privation de liberté(emprisonnement)'),
        ('privation ou restriction de droit', 'privation ou restriction de droit'),
    )

    # champ de model
    dateCondamnation = models.DateField(verbose_name='date de condamnation')
    organeCondamnatoire = models.CharField(verbose_name='cours ou tribunaux', max_length=100, default="cours de venise", blank=True, null=True)
    NatureCrime = models.CharField(verbose_name="natures du crime", max_length=15, choices=TYPE_DELIT)
    descriptionCrime = models.CharField(verbose_name='description crime', max_length=100, null=True, blank=True)
    dateCrime = models.DateField(verbose_name='date du crime ou délit')
    naturePeine = models.CharField(verbose_name='nature de la peine', max_length=100, choices=TYPE_DE_PEINE, blank=True, null=True)
    durePeine = models.IntegerField(verbose_name='durée des peines(en mois)', blank=True, null=True)
    observation = models.CharField(max_length=100, default='aucune')
    criminalprofile = ManyToManyField(CriminalProfil)

    def __str__(self):
        return 'comdamné le {} pour {}'.format(self.dateCondamnation, self.descriptionCrime)

    class Meta:
        ordering = ['-dateCondamnation']
