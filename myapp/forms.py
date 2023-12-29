from django import forms
from .models import *


class EmployeeAttendanceForm(forms.ModelForm):
    class Meta:
        model = Employee_Attendance
        fields = '__all__'

class LeavesForm(forms.ModelForm):
    class Meta:
        model = Leaves
        fields = '__all__'

class EmployeeLeavesForm(forms.ModelForm):
    class Meta:
        model = Employee_Leaves
        fields = '__all__'

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class EmployeeTrainingsForm(forms.ModelForm):
    class Meta:
        model = Employee_Trainings
        fields = '__all__'

class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = Employee_Salary
        fields = '__all__'

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeProjectForm(forms.ModelForm):
    class Meta:
        model = Employee_Project
        fields = '__all__'

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = Employee_Details
        fields = '__all__'

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = '__all__'


