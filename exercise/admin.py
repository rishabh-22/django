from django.contrib import admin
from exercise.models import Manager, Employee

# Register your models here.

class Mgr_list(admin.ModelAdmin):
    list_display = ['name', 'age', 'Department', 'created_date', 'modified_date']


class Emp_list(admin.ModelAdmin):
    list_display = ['name', 'age', 'salary', 'Designation', 'created_date', 'modified_date', 'reporting_manager']
    list_filter = ['age', 'salary']
    search_fields = ['name']
    fieldsets = (
        ('First Section', {'fields':('name', 'age')},),
        ('Second Section', {'fields':('salary', 'Designation')},),
        ('Third Section', {'fields':('reporting_manager',)},),
    )

admin.site.register(Manager, Mgr_list)
admin.site.register(Employee, Emp_list)




