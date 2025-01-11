from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, BlogViewSet, DoctorViewSet, ServiceReadOnlyViewSet, BlogReadOnlyViewSet, DoctorReadOnlyViewSet

router = DefaultRouter()

# Register both read-write and read-only viewsets with unique basenames
router.register(r'services', ServiceViewSet, basename='service')  # For full CRUD (read-write)
router.register(r'blogs', BlogViewSet, basename='blog')           # For full CRUD (read-write)
router.register(r'doctors', DoctorViewSet, basename='doctor')     # For full CRUD (read-write)

router.register(r'readonly-services', ServiceReadOnlyViewSet, basename='readonly-service')  # For read-only
router.register(r'readonly-blogs', BlogReadOnlyViewSet, basename='readonly-blog')        # For read-only
router.register(r'readonly-doctors', DoctorReadOnlyViewSet, basename='readonly-doctor')    # For read-only

urlpatterns = [
    # Other URLs
    path('api/', include(router.urls)),
]
