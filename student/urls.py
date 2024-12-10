from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentDetailsViewSet, SubjectViewSet, MarksViewSet
from .views import LoginView, TokenRefreshView


router = DefaultRouter()
router.register(r'students', StudentDetailsViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'marks', MarksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]