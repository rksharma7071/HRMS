from django.contrib import admin
from .models import *



@admin.register(Employee_Attendance)
class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display = ('emp', 'timeIn', 'timeOut', 'remarks')

@admin.register(Leaves)
class LeavesAdmin(admin.ModelAdmin):
    list_display = ('leaveName', 'days')

@admin.register(Employee_Leaves)
class EmployeeLeavesAdmin(admin.ModelAdmin):
    list_display = ('empId', 'leaveId', 'startDate', 'EndDate', 'totalDays')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author')

@admin.register(Employee_Trainings)
class EmployeeTrainingsAdmin(admin.ModelAdmin):
    list_display = ('emp', 'skills', 'training', 'projectReqt', 'bond')

@admin.register(Employee_Salary)
class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('emp', 'salaryRange', 'annualIncome', 'taxable', 'loans', 'insurance')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('positionName',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('departmentName',)

@admin.register(Employee_Project)
class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = ('emp', 'projectHandled', 'dateStarted', 'dateEnded', 'status')

@admin.register(Employee_Details)
class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('emp', 'firstName', 'middleName', 'lastName', 'positionId', 'deptId', 'birthDate', 'age', 'sex', 'address', 'employedDate', 'supervisorId', 'img')

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('title', 'startDate', 'endDate', 'createDate', 'description')