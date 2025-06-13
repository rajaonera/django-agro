from rest_framework import viewsets
from .models import Parcelle
from .serializers import ParcelleSerializer

class ParcelleViewSet(viewsets.ModelViewSet):
    queryset = Parcelle.objects.all()
    serializer_class = ParcelleSerializer

    # sécurisation : afficher uniquement les parcelles de l'utilisateur connecté
    def get_queryset(self):
        return Parcelle.objects.filter(user=self.request.user)

    # sécurisation : lier la parcelle créée à l'utilisateur connecté
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
