from django.db import models

class Parcelle(models.Model):
    nom = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
