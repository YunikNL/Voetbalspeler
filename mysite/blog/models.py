from django.conf import settings
from django.db import models
from django.utils import timezone

class Voetbalspeler(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        naam = models.CharField(max_length=100)
        actuele_voetbalclub = models.CharField(max_length=100)
        datum_invoer = models.DateTimeField(default=timezone.now)
        datum_laaste_aanpassing = models.DateTimeField(blank=True, null=True)

        def opslaan(self):
            self.datum_laaste_aanpassing = timezone.now()
            self.save()

        def __str__(self):
                return self.naam