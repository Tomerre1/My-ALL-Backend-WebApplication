from rest_framework import serializers
from .models import Level

#medicineName,description,level,count,badInfluence,foodOrNot

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        fields=['levelNumber','description']
    