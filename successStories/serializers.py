from rest_framework import serializers
from .models import SuccessStories


class SuccessStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=SuccessStories
        fields=['id','mail','title','mail','content','date']