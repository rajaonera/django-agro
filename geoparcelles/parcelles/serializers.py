from rest_framework import serializers
from .models import Parcelle, Observation

class ParcelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcelle
        fields =['id', 'nom', 'culture', 'date_creation'] 
        
class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'
