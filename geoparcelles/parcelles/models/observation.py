from django.db import models

class Observation(models.Model):
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE)
    date = models.DateField()
    note = models.TextField()

    def __str__(self):
        return f"Obs {self.parcelle.nom} - {self.date}"