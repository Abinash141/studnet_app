from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentDetailsViewSet, SubjectViewSet, MarksViewSet

router = DefaultRouter()
router.register(r'student', StudentDetailsViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'marks', MarksViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
