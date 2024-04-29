from django.forms import FileField, Form, ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["student_id", "first_name", "course_name", "mark"]

class UploadForm(Form):
    student_file = FileField()