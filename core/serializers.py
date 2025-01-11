from rest_framework import serializers
from .models import (
    Service, Blog, Consultant, HomeAboutHero, HomeServiceHeader, Speciality, HomeSpecialitiesHeader,
    HomeConsultantHeader, Equipment, EquipmentSpec, Testimonial
)
from django.utils.timesince import timesince

class HomeAboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAboutHero
        fields = ['id', 'title', 'description']

########################################################################################################

class HomeServiceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeServiceHeader
        fields = ['id', 'title', 'description']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'icon', 'title', 'description']
        
########################################################################################################

class HomeConsultantHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeConsultantHeader
        fields = ['id', 'title', 'description']

class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ['id', 'image', 'name', 'specialty']
        
########################################################################################################

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'image', 'author', 'category', 'title', 'date', 'description', 'is_featured']
        
class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ['id', 'image', 'name', 'specialty']
        
class HomeSpecialitiesHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSpecialitiesHeader
        fields = ['id', 'title', 'description']
        
class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'src', 'title', 'description']
        
class EquipmentSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentSpec
        fields = ['spec_name', 'spec_value']

class EquipmentSerializer(serializers.ModelSerializer):
    specifications = EquipmentSpecSerializer(many=True, read_only=True)

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'short_desc', 'description', 'image', 'color', 'specs']
    
class EquipmentReadonlySerializer(serializers.ModelSerializer):

    # Change the structure of specifications to a dictionary
    specs = serializers.SerializerMethodField()

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'short_desc', 'description', 'image', 'color', 'specs']

    def get_specs(self, obj):
        return {spec.spec_name: spec.spec_value for spec in obj.specifications.all()}
    
class BlogReadonlySerializer(serializers.ModelSerializer):
    time_ago = serializers.SerializerMethodField()
    is_latest = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d")  # To show only the date (no time)

    class Meta:
        model = Blog
        fields = ['id', 'image', 'author', 'category', 'title', 'date', 'description', 'is_featured', 'time_ago', 'is_latest']

    def get_time_ago(self, obj):
        """
        Returns a human-readable format like '6m ago', '1 hour ago', etc.
        """
        if obj.date:
            return timesince(obj.date) + " ago"
        return ""

    def get_is_latest(self, obj):
        """
        Returns True if this blog post is the most recent one.
        """
        latest_blog = Blog.objects.latest('created_at')
        return obj == latest_blog
    
    
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'treatment', 'content', 'rating', 'date']