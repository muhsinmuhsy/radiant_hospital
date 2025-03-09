from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import ( User,
    Service, Blog, Consultant, HomeAboutHero, HomeServiceHeader, Speciality, 
    HomeSpecialitiesHeader, Testimonial, SpecialitiesHero, SpecialitiesMainHeader, 
    ConsultantsMainHeader, HomeConsultantHeader, Equipment,
    ContactHero, QuickInfo, Mission, Vision,
    AboutHero, AboutStats, AboutCoreValues, 
    AboutFeatures, AboutAchievements, AboutContactDetails, DescCarousal, MobCarousal,
    Appointment, GetInTouch, ServiceHero
)
from .serializers import (
    ServiceSerializer, BlogSerializer, ConsultantSerializer, HomeAboutHeroSerializer, 
    HomeServiceHeaderSerializer, SpecialitySerializer, HomeSpecialitiesHeaderSerializer,
    HomeConsultantHeaderSerializer, EquipmentSerializer, EquipmentReadonlySerializer, 
    BlogReadonlySerializer, TestimonialSerializer, SpecialitiesHeroSerializer, 
    SpecialitiesMainHeaderSerializer, ConsultantsMainHeaderSerializer,
    ContactHeroSerializer,
    QuickInfoSerializer,
    MissionSerializer,
    VisionSerializer,
    AboutHeroSerializer, AboutStatsSerializer, AboutCoreValuesSerializer,
    AboutFeaturesSerializer, AboutAchievementsSerializer, AboutContactDetailsSerializer,
    DescCarousalSerializer, MobCarousalSerializer, AppointmentSerializer, GetInTouchSerializer,
    ServiceHeroSerializer, InquirySerializer
)
from rest_framework import generics
from django.core.mail import send_mail

# Login and Logout Views

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            request.user.auth_token.delete()  # Delete the token associated with the user
        return Response(status=status.HTTP_204_NO_CONTENT)


# Read-Write ViewSets (CRUD operations)

class DescCarousalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DescCarousal.objects.all()
    serializer_class = DescCarousalSerializer

class MobCarousallViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MobCarousal.objects.all()
    serializer_class = MobCarousalSerializer

class HomeAboutHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HomeAboutHero.objects.all()
    serializer_class = HomeAboutHeroSerializer

class HomeServiceHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HomeServiceHeader.objects.all()
    serializer_class = HomeServiceHeaderSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class HomeConsultantHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HomeConsultantHeader.objects.all()
    serializer_class = HomeConsultantHeaderSerializer

class ConsultantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer


class HomeSpecialitiesHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HomeSpecialitiesHeader.objects.all()
    serializer_class = HomeSpecialitiesHeaderSerializer

class SpecialitiesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class SpecialitiesHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SpecialitiesHero.objects.all()
    serializer_class = SpecialitiesHeroSerializer

class SpecialitiesMainHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SpecialitiesMainHeader.objects.all()
    serializer_class = SpecialitiesMainHeaderSerializer

class ConsultantsMainHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ConsultantsMainHeader.objects.all()
    serializer_class = ConsultantsMainHeaderSerializer

class ContactHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ContactHero.objects.all()
    serializer_class = ContactHeroSerializer

class QuickInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = QuickInfo.objects.all()
    serializer_class = QuickInfoSerializer

class MissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class VisionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Vision.objects.all()
    serializer_class = VisionSerializer

    
class AboutHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutHero.objects.all()
    serializer_class = AboutHeroSerializer

class AboutStatsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutStats.objects.all()
    serializer_class = AboutStatsSerializer

class AboutCoreValuesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutCoreValues.objects.all()
    serializer_class = AboutCoreValuesSerializer

class AboutFeaturesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutFeatures.objects.all()
    serializer_class = AboutFeaturesSerializer

class AboutAchievementsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutAchievements.objects.all()
    serializer_class = AboutAchievementsSerializer

class AboutContactDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutContactDetails.objects.all()
    serializer_class = AboutContactDetailsSerializer
    
class GetInTouchViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = GetInTouch.objects.all()
    serializer_class = GetInTouchSerializer
    
class ServiceHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ServiceHero.objects.all()
    serializer_class = ServiceHeroSerializer
    

# Read-Only ViewSets (viewsets.read-only access)

class DescCarousalReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DescCarousal.objects.all()
    serializer_class = DescCarousalSerializer
    
class MobCarousalReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MobCarousal.objects.all()
    serializer_class = MobCarousalSerializer

class HomeConsultantHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeConsultantHeader.objects.all()
    serializer_class = HomeConsultantHeaderSerializer

class HomeAboutHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeAboutHero.objects.all()
    serializer_class = HomeAboutHeroSerializer

class HomeServiceHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeServiceHeader.objects.all()
    serializer_class = HomeServiceHeaderSerializer

class ServiceReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ConsultantReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

class BlogReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogReadonlySerializer

class EquipmentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentReadonlySerializer

class HomeSpecialitiesHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeSpecialitiesHeader.objects.all()
    serializer_class = HomeSpecialitiesHeaderSerializer

class TestimonialReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class SpecialitiesMainHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpecialitiesMainHeader.objects.all()
    serializer_class = SpecialitiesMainHeaderSerializer

class SpecialitiesHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpecialitiesHero.objects.all()
    serializer_class = SpecialitiesHeroSerializer

class ConsultantsMainHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConsultantsMainHeader.objects.all()
    serializer_class = ConsultantsMainHeaderSerializer

class SpecialitiesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class ContactHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactHero.objects.all()
    serializer_class = ContactHeroSerializer

class QuickInfoReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuickInfo.objects.all()
    serializer_class = QuickInfoSerializer

class MissionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class VisionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vision.objects.all()
    serializer_class = VisionSerializer

class AboutHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutHero.objects.all()
    serializer_class = AboutHeroSerializer

class AboutStatsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutStats.objects.all()
    serializer_class = AboutStatsSerializer

class AboutCoreValuesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutCoreValues.objects.all()
    serializer_class = AboutCoreValuesSerializer

class AboutFeaturesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutFeatures.objects.all()
    serializer_class = AboutFeaturesSerializer

class AboutAchievementsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutAchievements.objects.all()
    serializer_class = AboutAchievementsSerializer

class AboutContactDetailsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutContactDetails.objects.all()
    serializer_class = AboutContactDetailsSerializer

class AppointmentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
class GetInTouchReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GetInTouch.objects.all()
    serializer_class = GetInTouchSerializer
    
class ServiceHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceHero.objects.all()
    serializer_class = ServiceHeroSerializer
    
# Create
class AppointmentCreateView(generics.CreateAPIView):
    """
    A view that only allows POST requests to create an appointment.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
class InquiryView(APIView):
    def post(self, request):
        serializer = InquirySerializer(data=request.data)
        if serializer.is_valid():
            full_name = serializer.validated_data["full_name"]
            email = serializer.validated_data["email"]
            phone = serializer.validated_data["phone"]
            message = serializer.validated_data["message"]

            # Send email
            send_mail(
                subject="New Medical Inquiry",
                message=f"Full Name: {full_name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
                from_email="your-email@example.com",  
                recipient_list=["info@radiantent.com"],
                fail_silently=False,
            )

            return Response({"message": "Inquiry submitted successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)