from rest_framework import serializers
from .models import (
    Service, Blog, Consultant, HomeAboutHero, HomeServiceHeader, Speciality, HomeSpecialitiesHeader,
    HomeConsultantHeader, Equipment, EquipmentSpec, Testimonial, SpecialitiesHero, SpecialitiesMainHeader,
    ConsultantsMainHeader, ContactHero, QuickInfo, Mission, Vision,
    AboutHero, DescCarousal, MobCarousal,
    Appointment, GetInTouch, ServiceHero, CTAButton, Inquiry, User
)
from django.utils.timesince import timesince
from django.contrib.auth.password_validation import validate_password

class DescCarousalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescCarousal
        fields = ['id', 'image']
        
class MobCarousalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobCarousal
        fields = ['id', 'image']

class HomeAboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAboutHero
        fields = '__all__'

class HomeServiceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeServiceHeader
        fields = ['id', 'title', 'description']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'icon', 'title', 'description']
        

class HomeConsultantHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeConsultantHeader
        fields = ['id', 'title', 'description']

class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ['id', 'image', 'name', 'specialty']
        

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'image', 'author', 'categories', 'title', 'date', 'description', 'is_featured']
        
class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = '__all__'
        
class HomeSpecialitiesHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSpecialitiesHeader
        fields = ['id', 'title', 'description']
        
class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'src', 'category', 'title', 'description', 'about', 'stat', 'benefits']
        
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
        fields = ['id', 'image', 'author', 'categories', 'title', 'date', 'description', 'is_featured', 'time_ago', 'is_latest']

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
        
class SpecialitiesHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialitiesHero
        fields = [
            'id',
            'simple_title',
            'title',
            'description',
            'specialties_count',
            'surgeries_count',
            'years_exp_count',
            'image',
            'image_badge_one',
            'image_badge_two',
        ]

class SpecialitiesMainHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialitiesMainHeader
        fields = [
            'id',
            'title',
            'description',
        ]
        

class ConsultantsMainHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantsMainHeader
        fields = ['id', 'title', 'description', 'mini_description']

class ContactHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactHero
        fields = [
            'id',
            'title_one',
            'title_two',
            'description',
        ]

class QuickInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickInfo
        fields = [
            'id',
            'contact',
            'hours',
            'location',
        ]

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = [
            'id',
            'title',
            'description',
        ]

class VisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vision
        fields = [
            'id',
            'title',
            'description',
        ]
        
class AboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHero
        fields = ['id', 'title', 'description']


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctors.name', read_only=True)
    class Meta:
        model = Appointment
        fields = '__all__'
        

class GetInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInTouch
        fields = '__all__'
        

class ServiceHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHero
        fields = ['id', 'title', 'description']
        
class InquirySerializer(serializers.ModelSerializer):
     class Meta:
        model = Inquiry
        fields = '__all__'
   
class CTAButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTAButton
        fields = '__all__'
        
class AppointmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['status']

class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'contact_number', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        validated_data['is_staff'] = True  # Ensure the user is marked as staff
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Update fields
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        
        # Handle password update
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "New password and confirm password do not match"})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect")
        return value

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user