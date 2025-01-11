from django.contrib import admin
from .models import Service, Blog, Doctor

# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_featured']
    list_filter = ['is_featured']
    search_fields = ['title', 'description']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty']
    search_fields = ['name', 'specialty']