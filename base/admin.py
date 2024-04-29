from django.contrib import admin

# Register your models here.

from .models import Student
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class StudentResource(resources.ModelResource):
    class Meta:
        model=Student
        fields=('student_id','first_name', 'last_name', 'course_name','mark')
        export_order =('student_id','first_name', 'last_name', 'course_name','mark')


admin.site.register(Student, ImportExportModelAdmin)