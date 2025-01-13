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
    ContactHero, QuickInfo, Mission, Vision, OurValues, CTASection,
    AboutHero, AboutStats, AboutCoreValues, 
    AboutFeatures, AboutAchievements, AboutContactDetails
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
    OurValuesSerializer,
    CTASectionSerializer,
    AboutHeroSerializer, AboutStatsSerializer, AboutCoreValuesSerializer,
    AboutFeaturesSerializer, AboutAchievementsSerializer, AboutContactDetailsSerializer
)

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
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()  # Delete the token associated with the user
        return Response(status=status.HTTP_204_NO_CONTENT)


# Read-Write ViewSets (CRUD operations)

class HomeConsultantHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HomeConsultantHeader.objects.all().order_by('-id')
    serializer_class = HomeConsultantHeaderSerializer

class HomeAboutHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HomeAboutHero.objects.all().order_by('-id')
    serializer_class = HomeAboutHeroSerializer

class HomeServiceHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HomeServiceHeader.objects.all().order_by('-id')
    serializer_class = HomeServiceHeaderSerializer

class SpecialitiesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Speciality.objects.all().order_by('-id')
    serializer_class = SpecialitySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all().order_by('-id')
    serializer_class = ServiceSerializer

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer

class ConsultantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Consultant.objects.all().order_by('-id')
    serializer_class = ConsultantSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Equipment.objects.all().order_by('-id')
    serializer_class = EquipmentSerializer
    
class AboutHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutHero.objects.all().order_by('-id')
    serializer_class = AboutHeroSerializer

class AboutStatsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutStats.objects.all().order_by('-id')
    serializer_class = AboutStatsSerializer

class AboutCoreValuesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutCoreValues.objects.all().order_by('-id')
    serializer_class = AboutCoreValuesSerializer

class AboutFeaturesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutFeatures.objects.all().order_by('-id')
    serializer_class = AboutFeaturesSerializer

class AboutAchievementsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutAchievements.objects.all().order_by('-id')
    serializer_class = AboutAchievementsSerializer

class AboutContactDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AboutContactDetails.objects.all().order_by('-id')
    serializer_class = AboutContactDetailsSerializer

# Read-Only ViewSets (viewsets.read-only access)

class HomeConsultantHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeConsultantHeader.objects.all().order_by('-id')
    serializer_class = HomeConsultantHeaderSerializer

class HomeAboutHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeAboutHero.objects.all().order_by('-id')
    serializer_class = HomeAboutHeroSerializer

class HomeServiceHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeServiceHeader.objects.all().order_by('-id')
    serializer_class = HomeServiceHeaderSerializer

class ServiceReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all().order_by('-id')
    serializer_class = ServiceSerializer

class ConsultantReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Consultant.objects.all().order_by('-id')
    serializer_class = ConsultantSerializer

class BlogReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogReadonlySerializer

class EquipmentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Equipment.objects.all().order_by('-id')
    serializer_class = EquipmentReadonlySerializer

class HomeSpecialitiesHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeSpecialitiesHeader.objects.all().order_by('-id')
    serializer_class = HomeSpecialitiesHeaderSerializer

class TestimonialReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.all().order_by('-id')
    serializer_class = TestimonialSerializer

class SpecialitiesMainHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpecialitiesMainHeader.objects.all().order_by('-id')
    serializer_class = SpecialitiesMainHeaderSerializer

class SpecialitiesHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpecialitiesHero.objects.all().order_by('-id')
    serializer_class = SpecialitiesHeroSerializer

class ConsultantsMainHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConsultantsMainHeader.objects.all().order_by('-id')
    serializer_class = ConsultantsMainHeaderSerializer

class SpecialitiesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Speciality.objects.all().order_by('-id')
    serializer_class = SpecialitySerializer

class ContactHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactHero.objects.all().order_by('-id')
    serializer_class = ContactHeroSerializer

class QuickInfoReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuickInfo.objects.all().order_by('-id')
    serializer_class = QuickInfoSerializer

class MissionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mission.objects.all().order_by('-id')
    serializer_class = MissionSerializer

class VisionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vision.objects.all().order_by('-id')
    serializer_class = VisionSerializer

class OurValuesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OurValues.objects.all().order_by('-id')
    serializer_class = OurValuesSerializer

class CTASectionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CTASection.objects.all().order_by('-id')
    serializer_class = CTASectionSerializer
    
class AboutHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutHero.objects.all().order_by('-id')
    serializer_class = AboutHeroSerializer

class AboutStatsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutStats.objects.all().order_by('-id')
    serializer_class = AboutStatsSerializer

class AboutCoreValuesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutCoreValues.objects.all().order_by('-id')
    serializer_class = AboutCoreValuesSerializer

class AboutFeaturesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutFeatures.objects.all().order_by('-id')
    serializer_class = AboutFeaturesSerializer

class AboutAchievementsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutAchievements.objects.all().order_by('-id')
    serializer_class = AboutAchievementsSerializer

class AboutContactDetailsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutContactDetails.objects.all().order_by('-id')
    serializer_class = AboutContactDetailsSerializer