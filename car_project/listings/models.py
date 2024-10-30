from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone = models.CharField(max_length=15, unique=True)  # Unique phone number
    my_location_link = models.URLField(blank=True, null=True)  
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True) 
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)  

    def _str_(self):
        return self.username
    
class OilType(models.Model):
    OIL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
    ]
    type = models.CharField(max_length=10, choices=OIL_CHOICES, unique=True)

    def __str__(self):
        return self.type

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name
class CarForSale(models.Model):
    OWNERSHIP_CHOICES = [
        ('1st', '1st Owner'),
        ('2nd', '2nd Owner'),
        ('3rd', '3rd Owner'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser instead of User
    name = models.CharField(max_length=100)  # Car name
    model_year = models.IntegerField()  # Year of manufacture
    km_driven = models.IntegerField()  # Kilometers driven
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # Link to Brand
    oil_type = models.ForeignKey(OilType, on_delete=models.CASCADE)  # Link to OilType
    accidental_background = models.BooleanField(default=False)  # Accidental background
    description = models.TextField()  # Car description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the car
    mileage = models.DecimalField(max_digits=5, decimal_places=2)  # Mileage of the car
    front_image = models.ImageField(upload_to='car_images/', blank=True, null=True)  # Front image
    leftside_img = models.ImageField(upload_to='car_images/', blank=True, null=True)  # Left side image
    rightside_img = models.ImageField(upload_to='car_images/', blank=True, null=True)  # Right side image
    back_image = models.ImageField(upload_to='car_images/', blank=True, null=True)  # Back image
    registration_number = models.CharField(max_length=20, unique=True)  # Registration number
    insurance_end_date = models.DateField()  # Insurance end date
    ownership_type = models.CharField(max_length=10, choices=OWNERSHIP_CHOICES)  # Ownership type
    created_date = models.DateField(auto_now_add=True)  # Date created
    created_time = models.TimeField(auto_now_add=True)  # Time created

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class CarForRent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser instead of User
    name = models.CharField(max_length=100)  # Car name
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # Link to Brand
    oil_type = models.ForeignKey(OilType, on_delete=models.CASCADE)  # Link to OilType
    description = models.TextField()  # Car description
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)  # Price per day for rent
    mileage = models.DecimalField(max_digits=5, decimal_places=2)  # Mileage of the car
    rent_car_image = models.ImageField(upload_to='car_rent_images/', blank=True, null=True)  # Rent car image
    created_date = models.DateField(auto_now_add=True)  # Date created
    created_time = models.TimeField(auto_now_add=True)  # Time created

    def __str__(self):
        return f"{self.name} - {self.user.username}"
