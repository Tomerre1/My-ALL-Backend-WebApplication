from rest_framework import serializers
from .models import Medicine

#medicineName,description,level,count,badInfluence,foodOrNot

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields=['medicineName','description','level','count','badInfluence','foodOrNot']
    