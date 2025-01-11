from rest_framework import serializers
from .models import Service, Blog, Doctor

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'image', 'title', 'description']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'image', 'author', 'category', 'title', 'date', 'description', 'is_featured']
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'image', 'name', 'specialty']