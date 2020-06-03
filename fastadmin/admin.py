from django.contrib import admin
from django.utils.safestring import mark_safe
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models import Employees, Departments, Cat


# Register your models here.
class DisplayEmployee(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name',
                    'birth_date', 'gender', 'hire_date')
    search_fields = ['first_name']
    list_filter = ('gender', ('birth_date', DateRangeFilter))
    ordering = ('last_name', 'hire_date')
    readonly_fields = ['emp_no', 'first_name']


class DisplayCat(admin.ModelAdmin):
    fields = ('name', 'age', 'photo')
    list_display = ('name', 'age', 'photo', 'get_image')

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=200,
            height=50,
        )
        )

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(Employees, DisplayEmployee)
admin.site.register(Departments)
admin.site.register(Cat, DisplayCat)
