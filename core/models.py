from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    contact_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.username
    
class HomeAboutHero(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About Us Hero Section"
        verbose_name_plural = "About Us Hero Sections"

    def __str__(self):
        return self.title or 'No Title'
    
class HomeServiceHeader(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Service Header"
        verbose_name_plural = "Service Headers"

    def __str__(self):
        return self.title or 'No Title'
    
class Service(models.Model):
    icon = models.FileField(upload_to='services/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


    def __str__(self):
        return self.title or 'No Title'
    
class HomeConsultantHeader(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Consultant Header"
        verbose_name_plural = "Consultant Headers"

    
class Consultant(models.Model):
    image = models.ImageField(upload_to='consultants/', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    specialty = models.CharField(max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Consultant"
        verbose_name_plural = "Consultants"


    def __str__(self):
        return self.name or 'No Name'
    
class Blog(models.Model):
    image = models.FileField(upload_to='blogs/', null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


    def __str__(self):
        return self.title or 'No Title'
    
class HomeSpecialitiesHeader(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Specialities Header"
        verbose_name_plural = "Specialities Headers"
        
    def __str__(self):
        return self.title or 'No Title'

    
class Speciality(models.Model):
    src = models.FileField(upload_to='services/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"

    
    def __str__(self):
        return self.title or 'No Title'
    
class Equipment(models.Model):
    name = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='equipment_images/')
    color = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"


    def __str__(self):
        return self.name

class EquipmentSpec(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='specifications', on_delete=models.CASCADE)
    spec_name = models.CharField(max_length=255)
    spec_value = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Equipment Specification"
        verbose_name_plural = "Equipment Specifications"

    def __str__(self):
        return f"{self.spec_name}: {self.spec_value}"
    
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"Testimonial by {self.name} for {self.treatment}"
    
    
class SpecialitiesHero(models.Model):
    simple_title = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    Specialties_count = models.CharField(max_length=100, null=True, blank=True)
    surgeries = models.CharField(max_length=100, null=True, blank=True)
    years_exp_count = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to="specialities_hero", null=True, blank=True)
    image_badge_one = models.CharField(max_length=100, null=True, blank=True)
    image_badge_two = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = "Specialities Hero"
        verbose_name_plural = "Specialities Heros"

    def __str__(self):
        return self.title or 'No Title'

class SpecialitiesMainHeader(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Specialities Main Header"
        verbose_name_plural = "Specialities Main Headers"

    def __str__(self):
        return self.title or 'No Title'