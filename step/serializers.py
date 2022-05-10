from rest_framework import serializers
from .models import Step,StepForUser

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model=Step
        fields=['levelNumber','stepNumber','description','requirements']

class StepForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=StepForUser
        fields=['mail','levelNumber','stepNumber','description','date','requirements','isDone','isCurrStep']
    