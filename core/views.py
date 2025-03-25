from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import ( User,
    Service, Blog, Consultant, HomeAboutHero, HomeServiceHeader, Speciality, 
    HomeSpecialitiesHeader, Testimonial, SpecialitiesHero, SpecialitiesMainHeader, 
    ConsultantsMainHeader, HomeConsultantHeader, Equipment,
    ContactHero, QuickInfo, Mission, Vision,
    AboutHero, DescCarousal, MobCarousal,
    Appointment, GetInTouch, ServiceHero, CTAButton, Inquiry
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
    AboutHeroSerializer,
    DescCarousalSerializer, MobCarousalSerializer, AppointmentSerializer, GetInTouchSerializer,
    ServiceHeroSerializer, InquirySerializer, CTAButtonSerializer, AppointmentStatusSerializer,
    StaffUserSerializer, ChangePasswordSerializer
)
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.shortcuts import get_object_or_404

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
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = DescCarousal.objects.all()
    serializer_class = DescCarousalSerializer

class MobCarousallViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = MobCarousal.objects.all()
    serializer_class = MobCarousalSerializer

class HomeAboutHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = HomeAboutHero.objects.all()
    serializer_class = HomeAboutHeroSerializer

class HomeServiceHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = HomeServiceHeader.objects.all()
    serializer_class = HomeServiceHeaderSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class HomeConsultantHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = HomeConsultantHeader.objects.all()
    serializer_class = HomeConsultantHeaderSerializer

class ConsultantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer


class HomeSpecialitiesHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = HomeSpecialitiesHeader.objects.all()
    serializer_class = HomeSpecialitiesHeaderSerializer

class SpecialitiesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class SpecialitiesHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = SpecialitiesHero.objects.all()
    serializer_class = SpecialitiesHeroSerializer

class SpecialitiesMainHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = SpecialitiesMainHeader.objects.all()
    serializer_class = SpecialitiesMainHeaderSerializer

class ConsultantsMainHeaderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = ConsultantsMainHeader.objects.all()
    serializer_class = ConsultantsMainHeaderSerializer

class ContactHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = ContactHero.objects.all()
    serializer_class = ContactHeroSerializer

class QuickInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = QuickInfo.objects.all()
    serializer_class = QuickInfoSerializer

class MissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class VisionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Vision.objects.all()
    serializer_class = VisionSerializer

    
class AboutHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = AboutHero.objects.all()
    serializer_class = AboutHeroSerializer

    
class GetInTouchViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = GetInTouch.objects.all()
    serializer_class = GetInTouchSerializer
    
class ServiceHeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = ServiceHero.objects.all()
    serializer_class = ServiceHeroSerializer
    
class CTAButtonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = CTAButton.objects.all()
    serializer_class = CTAButtonSerializer
    

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
    queryset = Equipment.objects.all().order_by('order')
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

class AppointmentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all().order_by('-id')
    serializer_class = AppointmentSerializer
    
class InquiryReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Inquiry.objects.all().order_by('-id')
    serializer_class = InquirySerializer
    
class GetInTouchReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GetInTouch.objects.all()
    serializer_class = GetInTouchSerializer
    
class ServiceHeroReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceHero.objects.all()
    serializer_class = ServiceHeroSerializer
    
class CTAButtonReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CTAButton.objects.all()
    serializer_class = CTAButtonSerializer
    
# Create
class AppointmentCreateView(generics.CreateAPIView):
    """
    A view that only allows POST requests to create an appointment.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
class UpdateAppointmentStatusView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        serializer = AppointmentStatusSerializer(appointment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Status updated successfully", "status": serializer.data["status"]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteAppointmentView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.delete()
        return Response({"message": "Appointment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class InquiryView(APIView):
    def post(self, request):
        serializer = InquirySerializer(data=request.data)
        if serializer.is_valid():
            inquiry = serializer.save()

            # Send email
            send_mail(
                subject="New Medical Inquiry",
                message=f"Full Name: {inquiry.full_name}\n"
                        f"Email: {inquiry.email}\n"
                        f"Phone: {inquiry.phone}\n"
                        f"Message: {inquiry.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,  
                recipient_list=["info@radiantent.com"],
                fail_silently=False,
            )

            return Response({"message": "Inquiry submitted successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Counts(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        appoiments = Appointment.objects.count()
        today_appoiments = Appointment.objects.filter(created_at__date=timezone.now().date()).count()
        inquires = Inquiry.objects.count()
        doctors = Consultant.objects.count()

        return Response({
            "total_appointments": appoiments,
            "today_appointments": today_appoiments,
            "total_inquiries": inquires,
            "total_doctors": doctors
        }, status=status.HTTP_200_OK)
        

# staff user
class StaffUserListView(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=True).exclude(is_superuser=True)
    serializer_class = StaffUserSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

class StaffUserCreateView(generics.CreateAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = StaffUserSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

class StaffUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = StaffUserSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_field = 'id'  # Retrieve & update by user ID

class CurrentUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "contact_number": user.contact_number,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser
        }
        return Response(data, status=status.HTTP_200_OK)
    
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)