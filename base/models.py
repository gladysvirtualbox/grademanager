from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=16)
    mark= models.CharField(max_length=100)
    

    def __str__(self):
        return str("{self.student_id} ({self.student_id})")
