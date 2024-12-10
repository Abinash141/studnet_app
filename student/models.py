from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class StudentDetails(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    password = models.CharField(max_length=255)  # Add password field
    

    def __str__(self):
        return self.name
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name

class Subject(models.Model):
    subject_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.subject_name

class Marks(models.Model):
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.subject_name}: {self.marks}"
