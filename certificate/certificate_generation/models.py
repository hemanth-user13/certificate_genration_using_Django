from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
class StudentData(models.Model):
    pin_number = models.CharField(max_length=20)
    student_full_name = models.CharField(max_length=100)
    student_father_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=7)
    date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20)  # Add admission number field
    gender = models.CharField(max_length=10)  # Add gender field
    religion = models.CharField(max_length=50)  # Add religion field
    nationality = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    tc_number = models.CharField(max_length=3)

    def __str__(self):
        return self.student_full_name