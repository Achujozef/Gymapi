from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)


from django.contrib.auth.models import User
from django.db import models

class GymUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Personal Information
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, default='')  # Assuming choices: Male, Female, Other
    date_of_birth = models.DateField(default='1900-01-01')
    contact_number = models.CharField(max_length=15, default='')
    email = models.EmailField(default='')
    address = models.TextField(default='')

    # Membership Information
    MEMBERSHIP_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Annual', 'Annual'),
        # Add more choices as needed
    ]
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES, default='')
    joining_date = models.DateField(default='1900-01-01')
    membership_expiry_date = models.DateField(default='1900-01-01')
    MEMBERSHIP_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Suspended', 'Suspended'),
    ]
    membership_status = models.CharField(max_length=20, choices=MEMBERSHIP_STATUS_CHOICES, default='')
    membership_plan = models.CharField(max_length=100, default='')

    # Health and Fitness Profile
    health_conditions = models.TextField(default='')
    fitness_goals = models.TextField(default='')
    workout_schedule = models.TextField(default='')
    exercise_restrictions = models.TextField(default='')

    # Emergency Contact Information
    emergency_contact_name = models.CharField(max_length=100, default='')
    emergency_contact_phone_number = models.CharField(max_length=15, default='')
    emergency_contact_relationship = models.CharField(max_length=100, default='')

    # Access Control
    membership_id_number = models.CharField(max_length=50, default='')
    access_information = models.CharField(max_length=100, default='RFID')  # RFID, Barcode, etc.

    # Personal Trainer Assignment
    assigned_personal_trainer = models.CharField(max_length=100, blank=True, null=True, default='')
    trainer_contact_information = models.CharField(max_length=100, blank=True, null=True, default='')

    # Locker Assignment
    assigned_locker_number = models.CharField(max_length=20, blank=True, null=True, default='')

    # Survey and Feedback Responses
    feedback = models.TextField(blank=True, null=True, default='')

    # Document Attachments
    documents = models.FileField(upload_to='documents/', blank=True, null=True)

        
class OTP(models.Model):
    phone = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.phone}"
    

class GymEquipment(models.Model):
    CATEGORY_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('free_weights', 'Free Weights'),
        ('machines', 'Machines'),
        ('other', 'Other'),
    ]
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('refurbished', 'Refurbished'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    manufacturer = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50)
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_information = models.TextField(blank=True, null=True)
    warranty_expiration_date = models.DateField(blank=True, null=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    maintenance_charge = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name