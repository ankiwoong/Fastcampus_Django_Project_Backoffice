from django.contrib import admin
from .models import Employees

# Register your models here.


class DisplayEmployee(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name',
                    'birth_date', 'gender', 'hire_date')
    search_fields = ['first_name']
    list_filter = ('gender',)
    ordering = ('last_name', 'hire_date')


admin.site.register(Employees, DisplayEmployee)
