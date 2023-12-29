from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

class Employee_Attendance(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    timeIn = models.DateField(auto_now_add=True)
    timeOut = models.DateField()
    remarks = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.emp
    

class Leaves(models.Model):
    leaveName = models.CharField(max_length=255)
    days = models.IntegerField()

    def __str__(self):
        return self.leaveName


class Employee_Leaves(models.Model):
    empId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    leaveId = models.ForeignKey(Leaves, on_delete=models.CASCADE, null=True, blank=True)
    startDate = models.DateField()
    EndDate = models.DateField()
    totalDays = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.emp} - {self.leaveId}"


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title    

class Holiday(models.Model):
    title = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    createDate = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title    


class Employee_Trainings(models.Model):
    emp = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.CharField(max_length=255)
    training = models.CharField(max_length=100)
    projectReqt = models.CharField(max_length=100)
    bond = models.IntegerField()

    def __str__(self):
        return f"{self.emp} - {self.skills}"


class Employee_Salary(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    salaryRange = models.CharField(max_length=100)
    annualIncome = models.IntegerField()
    taxable = models.IntegerField()
    loans = models.IntegerField()
    insurance = models.IntegerField()

    def __str__(self):
        return f"{self.emp} - {salaryRange}"
    

class Position(models.Model):
    positionName = models.CharField(max_length=100)

    def __str__(self):
        return self.positionName
    

class Department(models.Model):
    departmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.departmentName


class Employee_Project(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    projectHandled = models.CharField(max_length=100)
    dateStarted = models.DateField()
    dateEnded = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.emp} - {self.projectHandled} "


class Employee_Details(models.Model):
    GENDER_CHOICES = (
        ("", "Select Gender"),
        ("Male", "Male"),
        ("Female", "Female")
    )

    emp = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, null=True, blank=True, default="")
    lastName = models.CharField(max_length=100, null=True, blank=True, default="")
    deptId = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    positionId = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True) 
    birthDate = models.DateField()
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES, default="")
    address = models.CharField(max_length=255)
    employedDate = models.DateField()
    supervisorId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervised_employees', null=True, blank=True) 
    img = models.ImageField(upload_to='employee', null=True, blank=True)

    def __str__(self):
        return f"{self.firstName} {self.middleName} {self.lastName}"