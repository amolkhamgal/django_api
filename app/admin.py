from django.contrib import admin
from .models import Employee, Department

# Register your models here.
# company/admin.py


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department','salary','gender')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)

