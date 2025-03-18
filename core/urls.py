from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( 
    LoginView, LogoutView,
    MobCarousalReadOnlyViewSet, DescCarousalReadOnlyViewSet,
    ServiceViewSet, BlogViewSet, ConsultantViewSet, HomeAboutHeroViewSet,
    ServiceReadOnlyViewSet, BlogReadOnlyViewSet, HomeAboutHeroReadOnlyViewSet,
    HomeServiceHeaderViewSet, SpecialitiesViewSet, HomeServiceHeaderReadOnlyViewSet, SpecialitiesReadOnlyViewSet,
    HomeConsultantHeaderReadOnlyViewSet, ConsultantReadOnlyViewSet, HomeSpecialitiesHeaderReadOnlyViewSet,
    EquipmentViewSet, EquipmentReadOnlyViewSet, TestimonialReadOnlyViewSet,
    SpecialitiesMainHeaderReadOnlyViewSet, SpecialitiesHeroReadOnlyViewSet, ConsultantsMainHeaderReadOnlyViewSet,
    ContactHeroReadOnlyViewSet, QuickInfoReadOnlyViewSet, MissionReadOnlyViewSet,
    VisionReadOnlyViewSet,
    AboutHeroViewSet,
    AboutHeroReadOnlyViewSet, 
    DescCarousalViewSet,
    MobCarousallViewSet,
    HomeConsultantHeaderViewSet,
    HomeSpecialitiesHeaderViewSet,
    TestimonialViewSet,
    SpecialitiesHeroViewSet,
    SpecialitiesMainHeaderViewSet,
    ConsultantsMainHeaderViewSet,
    ContactHeroViewSet,
    QuickInfoViewSet,
    MissionViewSet,
    VisionViewSet,
    AppointmentReadOnlyViewSet,
    AppointmentCreateView,
    GetInTouchViewSet,
    GetInTouchReadOnlyViewSet,
    ServiceHeroViewSet,
    ServiceHeroReadOnlyViewSet,
    InquiryView,
    CTAButtonViewSet,
    CTAButtonReadOnlyViewSet,
    Counts,
    InquiryReadOnlyViewSet,
    UpdateAppointmentStatusView,
    StaffUserCreateView, StaffUserListView, StaffUserDetailView, CurrentUser
)

router = DefaultRouter()

# Register CRUD viewsets
router.register(r'home-about-hero', HomeAboutHeroViewSet, basename='home-about-hero')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'consultants', ConsultantViewSet, basename='consultant')
router.register(r'specialities', SpecialitiesViewSet, basename='specialities')
router.register(r'home-service-header', HomeServiceHeaderViewSet, basename='service-header')
router.register(r'equipments', EquipmentViewSet, basename='equipment')

router.register(r'about-hero', AboutHeroViewSet, basename='about-hero')

router.register(r'desc-carousal', DescCarousalViewSet, basename='desc-carousal')
router.register(r'mob-carousal', MobCarousallViewSet, basename='mob-carousal')
router.register(r'home-consultant-header', HomeConsultantHeaderViewSet, basename='home-consultant-header')
router.register(r'home-specialities-header', HomeSpecialitiesHeaderViewSet, basename='home-specialities-header')
router.register(r'testimonials', TestimonialViewSet, basename='testimonials')
router.register(r'specialities-hero', SpecialitiesHeroViewSet, basename='specialities-hero')
router.register(r'specialities-main-header', SpecialitiesMainHeaderViewSet, basename='specialities-main-header')
router.register(r'consultants-main-header', ConsultantsMainHeaderViewSet, basename='consultants-main-header')
router.register(r'contact-hero', ContactHeroViewSet, basename='contact-hero')
router.register(r'quick-info', QuickInfoViewSet, basename='quick-info')
router.register(r'mission', MissionViewSet, basename='mission')
router.register(r'vision', VisionViewSet, basename='vision')
router.register(r'get-in-touch', GetInTouchViewSet, basename='get-in-touch')
router.register(r'service-hero', ServiceHeroViewSet, basename='service-hero')
router.register(r'cta-button', CTAButtonViewSet, basename='cta-button')


# Register read-only viewsets
router.register(r'readonly-desc-carousal', DescCarousalReadOnlyViewSet, basename='readonly-desc-carousal')
router.register(r'readonly-mob-carousal', MobCarousalReadOnlyViewSet, basename='readonly-mob-carousal')
router.register(r'readonly-home-about-hero', HomeAboutHeroReadOnlyViewSet, basename='readonly-home-about-hero')
router.register(r'readonly-services', ServiceReadOnlyViewSet, basename='readonly-service')
router.register(r'readonly-blogs', BlogReadOnlyViewSet, basename='readonly-blog')
router.register(r'readonly-consultants', ConsultantReadOnlyViewSet, basename='readonly-consultant')
router.register(r'readonly-home-consultant-header', HomeConsultantHeaderReadOnlyViewSet, basename='consultant-header')
router.register(r'readonly-home-service-header', HomeServiceHeaderReadOnlyViewSet, basename='readonly-service-header')
router.register(r'readonly-specialities', SpecialitiesReadOnlyViewSet, basename='readonly-specialities')
router.register(r'readonly-home-specialities-header', HomeSpecialitiesHeaderReadOnlyViewSet, basename='readonly-specialities-header')
router.register(r'readonly-equipments', EquipmentReadOnlyViewSet, basename='readonly-equipment')
router.register(r'readonly-testimonials', TestimonialReadOnlyViewSet, basename='readonly-testimonial')
router.register(r'readonly-specialities-main-header', SpecialitiesMainHeaderReadOnlyViewSet, basename='readonly-specialities-main-header')
router.register(r'readonly-specialities-hero', SpecialitiesHeroReadOnlyViewSet, basename='readonly-specialities-hero')
router.register(r'readonly-consultants-main-header', ConsultantsMainHeaderReadOnlyViewSet, basename='readonly-consultants-main-header')

router.register(r'readonly-contact-hero', ContactHeroReadOnlyViewSet, basename='readonly-contact-hero')
router.register(r'readonly-quick-info', QuickInfoReadOnlyViewSet, basename='readonly-quick-info')
router.register(r'readonly-mission', MissionReadOnlyViewSet, basename='readonly-mission')
router.register(r'readonly-vision', VisionReadOnlyViewSet, basename='readonly-vision')

router.register(r'readonly-about-hero', AboutHeroReadOnlyViewSet, basename='readonly-about-hero')

router.register(r'readonly-appointments', AppointmentReadOnlyViewSet, basename='readonly-appointments')
router.register(r'readonly-get-in-touch', GetInTouchReadOnlyViewSet, basename='readonly-get-in-touch')
router.register(r'readonly-service-hero', ServiceHeroReadOnlyViewSet, basename='readonly-service-hero')
router.register(r'readonly-cta-button', CTAButtonReadOnlyViewSet, basename='readonly-cta-button')
router.register(r'readonly-inquiry', InquiryReadOnlyViewSet, basename='readonly-inquiry')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('appointment-create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path("appointments/<int:appointment_id>/status/", UpdateAppointmentStatusView.as_view(), name="update-appointment-status"),
    path("api/inquiry/", InquiryView.as_view(), name="inquiry_api"),
    
    path('counts/', Counts.as_view(), name='counts'),

    path('staff-users/', StaffUserListView.as_view(), name='staff-user-list'), 
    path('staff-users/create/', StaffUserCreateView.as_view(), name='staff-user-create'),
    path('staff-users/<int:id>/', StaffUserDetailView.as_view(), name='staff-user-detail'),
    path('current-user/', CurrentUser.as_view(), name='current-user'),

]
