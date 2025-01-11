from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework import status
from rest_framework import viewsets
from .models import Service, Blog, Consultant, HomeAboutHero, HomeServiceHeader, Speciality, HomeSpecialitiesHeader, Testimonial
from .serializers import (
    ServiceSerializer, BlogSerializer, ConsultantSerializer, HomeAboutHeroSerializer,
    HomeServiceHeaderSerializer, SpecialitySerializer, HomeSpecialitiesHeaderSerializer,
    HomeConsultantHeader, HomeConsultantHeaderSerializer, Equipment, EquipmentSerializer, EquipmentReadonlySerializer,
    BlogReadonlySerializer, TestimonialSerializer
    
)
# Create your views here.

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
        
# Read-Write ViewSets (for full CRUD operations)

class HomeAboutHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HomeAboutHero.objects.all()
    serializer_class = HomeAboutHeroSerializer
    
class HomeServiceHeaderViewSet(viewsets.ModelViewSet):
    queryset = HomeServiceHeader.objects.all()
    serializer_class = HomeServiceHeaderSerializer
    permission_classes = [IsAuthenticated]

class SpecialitiesViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = [IsAuthenticated]
    
class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ConsultantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

# Read-Only ViewSets (for read-only access)

class HomeAboutHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HomeAboutHeroSerializer

    def get_queryset(self):
        """
        Returns only the last created HomeAboutHero instance.
        """
        return HomeAboutHero.objects.order_by('-id')[:1]
    
class HomeServiceHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HomeServiceHeaderSerializer

    def get_queryset(self):
        """
        Returns all HomeServiceHeader ordered by the latest created first.
        """
        return HomeServiceHeader.objects.order_by('-created_at')
    
class ServiceReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
########################################################################################################

class HomeConsultantHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HomeConsultantHeaderSerializer

    def get_queryset(self):
        """
        Returns all HomeConsultantHeader ordered by the latest created first.
        """
        return HomeConsultantHeader.objects.order_by('-created_at')
    
class ConsultantReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    
class ServiceReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class BlogReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogReadonlySerializer

class ConsultantReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    
class HomeSpecialitiesHeaderReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HomeSpecialitiesHeaderSerializer

    def get_queryset(self):
        """
        Returns all HomeSpecialitiesHeader ordered by the latest created first.
        """
        return HomeSpecialitiesHeader.objects.order_by('-created_at')
    
class SpecialitiesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    
class EquipmentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentReadonlySerializer
    
class TestimonialReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer