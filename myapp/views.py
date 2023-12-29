from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from .forms import *


def view_home(request):
    return render(request, 'home.html', locals())


def view_signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username= username, password=password)

            if user is not None:
                login(request, user)
                message = "Login Successfully."
                return redirect('dashboard')
            else:
                message = "Invalid username or password."
                return  redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', locals())



def view_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        emp_form = EmployeeDetailsForm(request.POST)
        if form.is_valid() and emp_form.is_valid():
            user = form.save()
            employee = emp_form.save(commit=False)
            employee.emp = user
            employee.save()
            message = "Account created successfully"
            return redirect('dashboard')
    else:
        emp_form = EmployeeDetailsForm()
        form = UserCreationForm()

    return render(request, 'signup.html', locals())


def view_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    
    emp = Employee_Details.objects.get(emp=request.user)

    return render(request, 'dashboard.html', locals())

def view_employee(request):
    emp = Employee_Details.objects.get(emp=request.user)
    return render(request, 'employee.html', locals())


def view_leave(request):
    emp = Employee_Details.objects.get(emp=request.user)
    return render(request, 'leave.html', locals())


def view_attendance(request):
    emp = Employee_Details.objects.get(emp=request.user)
    return render(request, 'attendance.html', locals())


def view_holiday(request):
    holidays = Holiday.objects.all()
    return render(request, 'holiday.html', locals())


def view_logout(request):
    logout(request)
    return redirect('home')