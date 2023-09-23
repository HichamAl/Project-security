
from django.db import models

# Create your models here.

class VertrouwdePersonen(models.Model):
    bsn_nummer = models.CharField(primary_key=True, max_length=9)
    voornaam = models.CharField(max_length=128)
    achternaam = models.CharField(max_length=128)