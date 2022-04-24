from rest_framework import serializers
from .models import Tip


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tip
        fields=['id','mail','title','content','date','label']