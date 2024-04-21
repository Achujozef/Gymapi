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




class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'user', 'gym', 'branch', 'date', 'time']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'slot', 'user', 'date']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'gym', 'branch', 'day', 'start_time', 'end_time', 'available']

class ListBookingSerializer(serializers.ModelSerializer):
    slot_start_time = serializers.TimeField(source='slot.start_time')
    slot_end_time = serializers.TimeField(source='slot.end_time')
    slot_day = serializers.CharField(source='slot.get_day_display')

    class Meta:
        model = Booking
        fields = ['id', 'slot_start_time', 'slot_end_time', 'slot_day', 'date']


class GymPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymPlan
        fields = ['id', 'gym', 'branch', 'name', 'description', 'price', 'duration', 'duration_type','image','terms_and_conditions']


class GymPlanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymPlanPayment
        fields ='__all__'


class DietPlanTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlanTiming
        fields = ['id','time', 'item_name', 'is_done', 'description']

class DietPlanDaySerializer(serializers.ModelSerializer):
    timings = DietPlanTimingSerializer(many=True)

    class Meta:
        model = DietPlanDay
        fields = ['day', 'timings']

class DietPlanSerializer(serializers.ModelSerializer):
    days = DietPlanDaySerializer(many=True)

    class Meta:
        model = DietPlan
        fields = ['gym', 'branch', 'name', 'description', 'days']

    def create(self, validated_data):
        days_data = validated_data.pop('days')
        diet_plan = DietPlan.objects.create(**validated_data)
        for day_data in days_data:
            timings_data = day_data.pop('timings')
            diet_plan_day = DietPlanDay.objects.create(diet_plan=diet_plan, **day_data)
            for timing_data in timings_data:
                DietPlanTiming.objects.create(diet_plan_day=diet_plan_day, **timing_data)
        return diet_plan
    

class GymTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymTrainer
        fields = ['id', 'user', 'date_of_birth', 'contact_number', 'email', 'trainer_id', 'certification_level', 'certification_expiry_date', 'education_and_training_background', 'regular_working_hours', 'areas_of_expertise', 'specialized_certifications_or_skills', 'bio', 'profile_picture', 'salary', 'bonus_or_commission_information', 'documents', 'emergency_contact_information', 'health_conditions']