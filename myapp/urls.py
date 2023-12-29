"""
URL configuration for hrms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', view_home, name='home'),
    path('signin/', view_signin, name='signin'),
    path('signup/', view_signup, name='signup'),
    path('dashboard/', view_dashboard, name='dashboard'),
    path('employee/', view_employee, name='employee'),
    path('leave/', view_leave, name='leave'),
    path('attendance/', view_attendance, name='attendance'),
    path('holiday/', view_holiday, name='holiday'),
    path('logout/', view_logout, name='logout')
]
