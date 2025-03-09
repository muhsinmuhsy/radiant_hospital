from django.contrib import admin
from .models import (
    Service, Blog, Consultant, HomeConsultantHeader, HomeAboutHero, HomeServiceHeader, Speciality, HomeSpecialitiesHeader, Equipment, EquipmentSpec,
    Testimonial, SpecialitiesHero, SpecialitiesMainHeader, ConsultantsMainHeader,
    ContactHero, QuickInfo, Mission, Vision,
    AboutStats,
    AboutCoreValues,
    AboutFeatures,
    AboutAchievements,
    AboutContactDetails,
    DescCarousal, MobCarousal,
    Appointment, AboutHero,
    GetInTouch, ServiceHero
)
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy 

# Register your models here.

admin.site.site_header = "Radiant Hospital Admin"
admin.site.site_title = "Radiant Hospital Admin Portal"
admin.site.index_title = "Welcome to Radiant Hospital Administration"

admin.site.unregister(Group)
admin.site.unregister(TokenProxy)

@admin.register(DescCarousal)
class DescCarousalAdmin(admin.ModelAdmin):
    list_display = ['id']
    
@admin.register(MobCarousal)
class MobCarousalAdmin(admin.ModelAdmin):
    list_display = ['id']
    
@admin.register(HomeAboutHero)
class HomeAboutHeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(HomeServiceHeader)
class HomeServiceHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_featured']
    list_filter = ['is_featured', 'date']
    ordering = ['-id']
    search_fields = ['title', 'description']
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty']
    search_fields = ['name', 'specialty']
    list_filter = ['specialty']
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']
    
@admin.register(HomeConsultantHeader)
class HomeConsultantHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']
    
@admin.register(HomeSpecialitiesHeader)
class HomeSpecialitiesHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']
    
@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']

class EquipmentSpecInline(admin.TabularInline):
    model = EquipmentSpec
    extra = 1

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_desc', 'color']
    inlines = [EquipmentSpecInline]
    search_fields = ['name']
    ordering = ['-id']

admin.site.register(Equipment, EquipmentAdmin)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'treatment', 'rating', 'date']
    search_fields = ['name', 'treatment', 'content']
    list_filter = ['rating', 'date']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(SpecialitiesHero)
class SpecialitiesHeroAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'simple_title',
        'specialties_count',
        'surgeries_count',
        'years_exp_count',
    ]
    search_fields = [
        'title',
        'simple_title',
        'specialties_count',
    ]
    list_filter = [
        'specialties_count',
    ]
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(SpecialitiesMainHeader)
class SpecialitiesMainHeaderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'title',
        'description',
    ]
    ordering = ['-id']
    readonly_fields = ['created_at', 'updated_at']    
    
@admin.register(ConsultantsMainHeader)
class ConsultantsMainHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'mini_description', 'created_at', 'updated_at']
    search_fields = ['title', 'mini_description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-id',]
    readonly_fields = ['created_at', 'updated_at']

@admin.register(ContactHero)
class ContactHeroAdmin(admin.ModelAdmin):
    list_display = ['title_one', 'title_two', 'created_at', 'updated_at']
    search_fields = ['title_one', 'title_two']

@admin.register(QuickInfo)
class QuickInfoAdmin(admin.ModelAdmin):
    list_display = ['contact', 'hours', 'location', 'created_at', 'updated_at']
    search_fields = ['contact', 'location']

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']

# Admin for AboutStats
@admin.register(AboutStats)
class AboutStatsAdmin(admin.ModelAdmin):
    list_display = ['label', 'number', 'created_at', 'updated_at']  # Fields to display in the list view
    search_fields = ['label']  # Searchable fields
    list_filter = ['created_at', 'updated_at']  # Filters
    ordering = ['-created_at']  # Default ordering

# Admin for AboutCoreValues
@admin.register(AboutCoreValues)
class AboutCoreValuesAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']

# Admin for AboutFeatures
@admin.register(AboutFeatures)
class AboutFeaturesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']

# Admin for AboutAchievements
@admin.register(AboutAchievements)
class AboutAchievementsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']

# Admin for AboutContactDetails
@admin.register(AboutContactDetails)
class AboutContactDetailsAdmin(admin.ModelAdmin):
    list_display = ['phone', 'mail', 'location', 'time', 'created_at', 'updated_at']
    search_fields = ['phone', 'mail', 'location', 'time']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'preferred_date', 'preferred_time', 'created_at', 'updated_at']
    ordering = ['-id']
    
admin.site.register(AboutHero)
admin.site.register(GetInTouch)
admin.site.register(ServiceHero)