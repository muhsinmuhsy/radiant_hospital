from django.contrib import admin
from .models import (
    Service, Blog, Consultant, HomeConsultantHeader, HomeAboutHero, HomeServiceHeader, Speciality, HomeSpecialitiesHeader, Equipment, EquipmentSpec,
    Testimonial
)
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy 

# Register your models here.

admin.site.site_header = "Radiant Hospital Admin"
admin.site.site_title = "Radiant Hospital Admin Portal"
admin.site.index_title = "Welcome to Radiant Hospital Administration"

admin.site.unregister(Group)
admin.site.unregister(TokenProxy)

@admin.register(HomeAboutHero)
class HomeAboutHeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    ordering = ['-id']

@admin.register(HomeServiceHeader)
class HomeServiceHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-id']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    ordering = ['-id']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_featured']
    list_filter = ['is_featured', 'date']
    ordering = ['-id']
    search_fields = ['title', 'description']
    ordering = ['-id']

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty']
    search_fields = ['name', 'specialty']
    list_filter = ['specialty']
    ordering = ['-id']
    
@admin.register(HomeConsultantHeader)
class HomeConsultantHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-id']
    
@admin.register(HomeSpecialitiesHeader)
class HomeSpecialitiesHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-id']
    
@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    ordering = ['-id']

class EquipmentSpecInline(admin.TabularInline):
    model = EquipmentSpec
    extra = 1

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_desc', 'color')
    inlines = [EquipmentSpecInline]
    search_fields = ['name']
    ordering = ['-id']

admin.site.register(Equipment, EquipmentAdmin)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'treatment', 'rating', 'date']
    search_fields = ['name', 'treatment', 'content']
    list_filter = ['rating', 'date']