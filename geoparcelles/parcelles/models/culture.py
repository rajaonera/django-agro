from django.db import models

class Culture(models.Model):
    nom = models.CharField(max_length=100)
    periode_semis = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
