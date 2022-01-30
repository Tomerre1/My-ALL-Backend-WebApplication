from rest_framework import serializers
from .models import Medicine,MedicineForUser

#medicineName,description,level,count,badInfluence,foodOrNot

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields=['medicineName','description','levels','count','badInfluence','foodOrNot',"days"]

class MedicineForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicineForUser
        fields=['mail','medicineName','count','days']
    