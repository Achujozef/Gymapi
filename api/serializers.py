from rest_framework import serializers
from .models import GymUser

class GymUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymUser
        fields = '__all__'
