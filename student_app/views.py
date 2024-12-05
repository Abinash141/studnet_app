from django.shortcuts import render
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
