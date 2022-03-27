from rest_framework import serializers
from .models import Workshop


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Workshop
        fields=['id','mail','content','title','lecturer','date','isDone']