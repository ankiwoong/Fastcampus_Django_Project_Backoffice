from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models import Employees


# Register your models here.
class DisplayEmployee(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name',
                    'birth_date', 'gender', 'hire_date')
    search_fields = ['first_name']
    list_filter = ('gender', ('birth_date', DateRangeFilter))
    ordering = ('last_name', 'hire_date')


admin.site.register(Employees, DisplayEmployee)
