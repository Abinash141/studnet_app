from django.db import models

class StudentDetails(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField(null=True, blank=True)

    def clean(self):
        if self.marks is not None and (self.marks < 0 or self.marks > 100):
            raise ValidationError('Marks must be between 0 and 100.') # type: ignore

    def __str__(self):
        return f'{self.student.name} - {self.subject.name}'
