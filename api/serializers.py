from rest_framework import serializers
from .models import *

class GymUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymUser
        fields = '__all__'

class GymEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymEquipment
        fields = '__all__'

class BasicGymEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymEquipment
        fields = ['id', 'name', 'image', 'additional_notes']

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'
class EnquiryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        exclude = ['branch', 'added_by', 'gym']

class GymUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymUser
        fields = '__all__'