from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_dashboard, name='main_dashboard'),
    path('user_login/', views.user_login, name='user_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('excel_data/', views.excel_data, name='excel_data'),
]
