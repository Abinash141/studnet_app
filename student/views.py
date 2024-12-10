from rest_framework import viewsets
from .models import StudentDetails, Subject, Marks
from .serializers import StudentDetailsSerializer, SubjectSerializer, MarksSerializer

class StudentDetailsViewSet(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from rest_framework.response import Response
from .models import StudentDetails

class LoginView(TokenObtainPairView):
    """
    This view will issue JWT tokens (access and refresh tokens) upon successful login.
    """

    def post(self, request, *args, **kwargs):
        roll_no = request.data.get('roll_no')
        password = request.data.get('password')

        try:
            student = StudentDetails.objects.get(roll_no=roll_no)

            if student.check_password(password):
                return super().post(request, *args, **kwargs)  # Use the JWT token generation
            else:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        except StudentDetails.DoesNotExist:
            return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

class TokenRefreshView(TokenRefreshView):
    """
    This view will refresh the JWT token using the refresh token.
    """
    pass