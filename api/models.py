from django.db import models
from django.contrib.auth.models import User


class Gym(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Default owner ID, change as needed
    name = models.CharField(max_length=100, default="Gym Name")
    address = models.CharField(max_length=100, default="Address")
    phone_number = models.CharField(max_length=15, default="1234567890")
    email = models.EmailField(default="gym@example.com")
    has_branches = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Branch(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100, default='Branch Name')
    address = models.CharField(max_length=100, default='Branch Address')
    phone_number = models.CharField(max_length=15, default='Branch Phone Number')
    email = models.EmailField(default='branch@example.com')
    
    def __str__(self):
        return f"{self.name} - {self.gym.name}"

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=100, default='') 
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    hire_date = models.DateField(default='1900-01-01') 

    def __str__(self):
        return f"{self.user.username} - {self.gym.name}"

class Member(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user =  models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.gym.name}"


class GymTrainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    trainer_id = models.CharField(max_length=100)
    certification_level = models.CharField(max_length=100)
    certification_expiry_date = models.DateField()
    education_and_training_background = models.TextField()
    regular_working_hours = models.CharField(max_length=100)
    areas_of_expertise = models.TextField()
    specialized_certifications_or_skills = models.TextField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='trainer_profile_pictures/', blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_or_commission_information = models.CharField(max_length=100, blank=True, null=True)
    documents = models.FileField(upload_to='trainer_documents/', blank=True, null=True)
    emergency_contact_information = models.CharField(max_length=100)
    health_conditions = models.TextField()

    def __str__(self):
        return f"(Trainer ID: {self.trainer_id})"

class GymPlan(models.Model):
    DURATION_CHOICES = [
        ('day', 'Day'),
        ('month', 'Month'),
        ('year', 'Year'),
        ('lifetime', 'Lifetime'),
    ]
    
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, default='Standard Plan')
    description = models.TextField(default='Basic gym membership plan')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duration = models.PositiveIntegerField(default=1) 
    duration_type = models.CharField(max_length=10, choices=DURATION_CHOICES, default='month')
    image = models.ImageField(upload_to='gym_plan_images', null=True, blank=True) 
    terms_and_conditions = models.TextField(default='', blank=True)


class PlanFeature(models.Model):
    plan = models.ForeignKey(GymPlan, on_delete=models.CASCADE, related_name='features')
    feature = models.CharField(max_length=255)

    def __str__(self):
        return self.feature


class GymUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='')  
    date_of_birth = models.DateField(default='1900-01-01')
    contact_number = models.CharField(max_length=15, default='')
    email = models.EmailField(default='')
    address = models.TextField(default='')
    membership_type = models.ForeignKey(GymPlan, on_delete=models.SET_NULL, null=True, blank=True)
    joining_date = models.DateField(default='1900-01-01')
    membership_expiry_date = models.DateField(default='1900-01-01')
    MEMBERSHIP_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Suspended', 'Suspended'),
    ]
    is_active = models.BooleanField(default=True)
    health_conditions = models.TextField(default='')
    fitness_goals = models.TextField(default='')
    workout_schedule = models.TextField(default='')
    exercise_restrictions = models.TextField(default='')
    emergency_contact_name = models.CharField(max_length=100, default='')
    emergency_contact_phone_number = models.CharField(max_length=15, default='')
    emergency_contact_relationship = models.CharField(max_length=100, default='')
    membership_id_number = models.CharField(max_length=50, default='')
    access_information = models.CharField(max_length=100, default='RFID')  # RFID, Barcode, etc.
    assigned_personal_trainer = models.CharField(max_length=100, blank=True, null=True, default='')
    trainer_contact_information = models.CharField(max_length=100, blank=True, null=True, default='')
    assigned_locker_number = models.CharField(max_length=20, blank=True, null=True, default='')
    feedback = models.TextField(blank=True, null=True, default='')
    documents = models.FileField(upload_to='documents/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='user_profile_pictures/', blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    proffession = models.CharField(max_length=100, default='')



class UserWeight(models.Model):
    user = models.ForeignKey(GymUser, on_delete=models.CASCADE, related_name='weights')
    weight = models.FloatField()
    measured_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.weight} kg - {self.measured_at}"
    
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
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE,null=True, blank=True, default=None)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, default=None)
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
    image = models.ImageField(upload_to='gym_eqp_pictures/', blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)



class Enquiry(models.Model):
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Anonymous')
    phone_number = models.CharField(max_length=15, default='')
    place = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    plan = models.ForeignKey('GymPlan', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    expected_joining_date = models.DateField(default='1900-01-01')
    follow_up_date = models.DateField(default='1900-01-01')
    enquiry_source = models.CharField(max_length=100, default='')
    remarks = models.TextField(default='')
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, default=None)


class GymOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    gym_name = models.CharField(max_length=100, default='Default Gym Name')  
    state = models.CharField(max_length=100, default='')  
    district = models.CharField(max_length=100, default='')  
    city = models.CharField(max_length=100, default='')  
    gym_contact = models.CharField(max_length=15, blank=True, null=True)  
    branch_count = models.IntegerField(default=0) 

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('fees', 'Fees'),
        ('salary', 'Salary'),
        ('maintenance', 'Equipment Maintenance'),
        ('other_expense', 'Other Expense'),
    ]

    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    description = models.TextField(default='')
    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.date}"


class FeesTransaction(Transaction):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(GymPlan, on_delete=models.CASCADE)

class SalaryTransaction(Transaction):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class MaintenanceTransaction(Transaction):
    equipment = models.ForeignKey(GymEquipment, on_delete=models.CASCADE)

class OtherExpenseTransaction(Transaction):
    pass



class Slot(models.Model):
    DAY_CHOICES = [
        ('all', 'All'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, null=True, blank=True)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_day_display()} - {self.start_time} to {self.end_time}"

class Booking(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    booked_date = models.DateField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return f"{self.slot} - {self.user.username} - {self.date}"
    



class GymPlanPayment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, null=True, blank=True)
    gym_plan = models.ForeignKey('GymPlan', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    screenshot = models.ImageField(upload_to='payments/screenshots/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Payment for {self.gym_plan.name} by {self.user.username}"



class DietPlan(models.Model):
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DietPlanDay(models.Model):
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE, related_name='days')
    day = models.CharField(max_length=20)  
    
    def __str__(self):
        return f"{self.diet_plan.name} - {self.day}"

class DietPlanTiming(models.Model):
    diet_plan_day = models.ForeignKey(DietPlanDay, on_delete=models.CASCADE, related_name='timings')
    time = models.TimeField()
    item_name = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.diet_plan_day.day} - {self.time.strftime('%H:%M')}"


class DietAssignment(models.Model):
    user = models.ForeignKey(GymUser, on_delete=models.CASCADE)
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.diet_plan.name}" 