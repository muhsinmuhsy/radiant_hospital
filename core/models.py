from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    contact_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.username

#######################################################################################################

class DescCarousal(models.Model):
    image = models.FileField(upload_to="desc-carousal/")
    
class MobCarousal(models.Model):
    image = models.FileField(upload_to="mob-carousal/")
    
class HomeAboutHero(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    mini_text = models.CharField(max_length=255, null=True, blank=True)
    
    feature_one_name = models.CharField(max_length=255, null=True, blank=True)
    feature_one_description = models.CharField(max_length=255, null=True, blank=True)
    
    feature_two_name = models.CharField(max_length=255, null=True, blank=True)
    feature_two_description = models.CharField(max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Home About Us Hero Section"
        verbose_name_plural = "Home About Us Hero Sections"

    def __str__(self):
        return self.title or 'No Title'
    
class HomeServiceHeader(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Home Service Header"
        verbose_name_plural = "Home Service Headers"

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
        verbose_name = "Home Consultant Header"
        verbose_name_plural = "Home Consultant Headers"

    
class Consultant(models.Model):
    image = models.ImageField(upload_to='consultants/', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    specialty = models.CharField(max_length=255, null=True, blank=True)
    qualification = models.TextField(null=True, blank=True)
    experience = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    specialized_departments = models.JSONField(default=list, null=True, blank=True)
    # specializedDepartments: [
    #     "Pediatric ENT",
    #     "Sinus Surgery",
    #     "Hearing Restoration",
    #     "Voice and Swallowing Disorders",
    #     "Allergy Treatment"
    # ]
    available_days = models.JSONField(default=list, null=True, blank=True) 
    # [
    #     {
    #         "day": "Monday",
    #         "timeSlots": [
    #         { "time": "9:00 AM - 12:00 PM", "type": "Consultation" },
    #         { "time": "2:00 PM - 5:00 PM", "type": "Surgical Procedures" }
    #         ]
    #     },
    #     {
    #         "day": "Wednesday",
    #         "timeSlots": [
    #         { "time": "10:00 AM - 1:00 PM", "type": "Hearing Tests" },
    #         { "time": "4:00 PM - 7:00 PM", "type": "Evening Consultation" }
    #         ]
    #     },
    #     {
    #         "day": "Friday",
    #         "timeSlots": [
    #         { "time": "8:00 AM - 11:00 AM", "type": "Sinus Evaluation" },
    #         { "time": "3:00 PM - 6:00 PM", "type": "Allergy Consultation" }
    #         ]
    #     }
    # ]

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
    categories = models.JSONField(default=list, null=True, blank=True)
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
    
    def full_clean(self, *args, **kwargs):
        # If this blog is being set as featured, ensure others are not featured
        if self.is_featured:
            Blog.objects.filter(is_featured=True).exclude(id=self.id).update(is_featured=False)
        super().full_clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Ensure full_clean is called before saving
        self.full_clean()
        super().save(*args, **kwargs)
    
class HomeSpecialitiesHeader(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Home Specialities Header"
        verbose_name_plural = "Home Specialities Headers"
        
    def __str__(self):
        return self.title or 'No Title'

class Speciality(models.Model):
    CATEGORY_CHOICE  = (
        ("Surgical Procedures", "Surgical Procedures"),
        ("Endoscopic Surgery", "Endoscopic Surgery"),
    )
    src = models.FileField(upload_to='speciality/', null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True, choices=CATEGORY_CHOICE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    stat =  models.TextField(null=True, blank=True)
    benefits = models.JSONField(default=list, null=True, blank=True)
    
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
    image = models.ImageField(upload_to='equipment/')
    color = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)
    
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

####################################################################################################### 
    
class SpecialitiesHero(models.Model):
    simple_title = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    specialties_count = models.CharField(max_length=100, null=True, blank=True)
    surgeries_count = models.CharField(max_length=100, null=True, blank=True)
    years_exp_count = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to="specialities_hero", null=True, blank=True)
    image_badge_one = models.CharField(max_length=100, null=True, blank=True)
    image_badge_two = models.CharField(max_length=100, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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

#######################################################################################################
  
class ConsultantsMainHeader(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    mini_description =  models.CharField(max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Consultants Main Header"
        verbose_name_plural = "Consultants Main Headers"

    def __str__(self):
        return self.title or 'No Title'

#######################################################################################################
   
class ContactHero(models.Model):
    title_one = models.CharField(max_length=255)
    title_two =  models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Contact Hero"
        verbose_name_plural = "Contact Heros"

    def __str__(self):
        return self.title_one or 'No Title'
    
class QuickInfo(models.Model):
    contact = models.CharField(max_length=255)
    hours = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "QuickInfo"
        verbose_name_plural = "QuickInfos"

    def __str__(self):
        return self.contact or 'No Contact'

class AboutHero(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title or 'No Title'
    
class Mission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    list = models.JSONField(default=list, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Mission"
        verbose_name_plural = "Missions"

    def __str__(self):
        return self.title or 'No Title'
    
class Vision(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    list = models.JSONField(default=list, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Vission"
        verbose_name_plural = "Vissions"

    def __str__(self):
        return self.title or 'No Title'
    
class CTAButton(models.Model):
    single_title = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#######################################################################################################

class Appointment(models.Model):
    full_name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(max_length=225, null=True, blank=True)
    phone = models.CharField(max_length=225, null=True, blank=True)
    age = models.CharField(max_length=225, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    doctors = models.ForeignKey(Consultant, on_delete=models.SET_NULL, null=True, blank=True)
    preferred_date = models.CharField(max_length=225, null=True, blank=True)
    preferred_time = models.CharField(max_length=225, null=True, blank=True)
    status =models.CharField(max_length=225, default="Pending", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

#######################################################################################################

class GetInTouch(models.Model):
    location = models.CharField(max_length=255, help_text="Physical address of the company")
    phone = models.CharField(max_length=20, help_text="Contact phone number")
    email = models.EmailField(help_text="Contact email address")
    working_hours = models.CharField(max_length=255, help_text="Company working hours")

    def __str__(self):
        return self.location

class ServiceHero(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Service Hero"
        verbose_name_plural = "Service Heros"

    def __str__(self):
        return self.title or 'No Title'
    
#######################################################################################################
    
class Inquiry(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)