from django.db import models
from django.contrib.auth.models import User  

# parcelle de terre lier a un utilisateur
class Parcelle(models.Model):
    nom = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parcelles",default=1)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.nom
