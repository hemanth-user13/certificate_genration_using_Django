from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import StudentData  # Import your StudentData model

def main_dashboard(request):
    return render(request, 'main_dashboard.html')

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        superuser = User.objects.filter(username=username, is_superuser=True).first()

        if superuser:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                # Add an error message for incorrect credentials
                messages.error(request, 'Incorrect username or password.')

    return render(request, 'main_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StudentData

def generate_certificate(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        student = StudentData.objects.filter(pin_number=roll_number).first()

        if student:
            certificate_type = request.POST.get('certificate_type')

            if certificate_type == 'study_and_conduct':
                return render(request, 'study_and_conduct_certificate.html', {'student': student})
            elif certificate_type == 'tc':
                return render(request, 'tc.html', {'student': student})
            elif certificate_type == 'custodian':
                return render(request, 'custodian_certificate.html', {'student': student})
            elif certificate_type == 'course_completion':
                return render(request, 'course_completion_certificate.html', {'student': student})
            elif certificate_type=='english_proficiency':
                return render(request,'english_proficiency_cerificate.html',{'student':student})
            else:
                return HttpResponse("Invalid certificate type")
        else:
            return render(request, 'admin_dashboard.html', {'error_message': 'Student not found'})

    return redirect('admin_dashboard')

import pandas as pd
import random
from .models import StudentData
from django.shortcuts import render, redirect
from datetime import datetime

# ...

def excel_data(request):
    error_message = None
    success_message = None  # Initialize success message variable
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        if excel_file.name.endswith('.xlsx'):
            df = pd.read_excel(excel_file, engine='openpyxl')
            for index, row in df.iterrows():
                date_of_birth = str(row['DOB'])
                academic_year = row['ACADEMIC PERIOD']
                if academic_year:
                    student_data = StudentData(
                        pin_number=row['PIN NO'],
                        student_full_name=row['NAME OF THE STUDENT'],
                        student_father_name=row['FATHER NAME'],
                        department=row['BRANCH NAME'],
                        academic_year=academic_year,
                        date_of_birth=date_of_birth,
                        place=row['PLACE'],
                        admission_number=row['ADMN NUMBER'],
                        gender=row['GENDER'],
                        religion=row['RELIGION'],
                        nationality=row['NATIONALITY'],
                        tc_number=str(random.randint(100, 999))
                    )
                    student_data.save()
                else:
                    error_message = 'Invalid academic year format in Excel file.'
                    return render(request, 'excel_data.html', {'error_message': error_message})
            success_message = 'Data uploaded successfully'  # Set the success message
            return render(request, 'excel_data.html', {'success_message': success_message})
        else:
            error_message = 'Please upload a valid Excel file.'
    return render(request, 'excel_data.html', {'error_message': error_message})
