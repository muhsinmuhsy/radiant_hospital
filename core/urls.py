from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( 
    LoginView, LogoutView,
    ServiceViewSet, BlogViewSet, ConsultantViewSet, HomeAboutHeroViewSet,
    ServiceReadOnlyViewSet, BlogReadOnlyViewSet, HomeAboutHeroReadOnlyViewSet,
    HomeServiceHeaderViewSet, SpecialitiesViewSet, HomeServiceHeaderReadOnlyViewSet, SpecialitiesReadOnlyViewSet,
    HomeConsultantHeaderReadOnlyViewSet, ConsultantReadOnlyViewSet, HomeSpecialitiesHeaderReadOnlyViewSet,
    EquipmentViewSet, EquipmentReadOnlyViewSet, TestimonialReadOnlyViewSet,
    SpecialitiesMainHeaderReadOnlyViewSet, SpecialitiesHeroReadOnlyViewSet, ConsultantsMainHeaderReadOnlyViewSet,
    ContactHeroReadOnlyViewSet, QuickInfoReadOnlyViewSet, MissionReadOnlyViewSet,
    VisionReadOnlyViewSet, OurValuesReadOnlyViewSet, CTASectionReadOnlyViewSet
)

router = DefaultRouter()

# Register CRUD viewsets
router.register(r'about-hero', HomeAboutHeroViewSet, basename='about-hero')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'consultants', ConsultantViewSet, basename='consultant')
router.register(r'specialities', SpecialitiesViewSet, basename='specialities')
router.register(r'home-service-header', HomeServiceHeaderViewSet, basename='service-header')
router.register(r'equipments', EquipmentViewSet, basename='equipment')

# Register read-only viewsets
router.register(r'readonly-home-about-hero', HomeAboutHeroReadOnlyViewSet, basename='readonly-about-hero')
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
router.register(r'readonly-our-values', OurValuesReadOnlyViewSet, basename='readonly-our-values')
router.register(r'readonly-cta-section', CTASectionReadOnlyViewSet, basename='readonly-cta-section')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
