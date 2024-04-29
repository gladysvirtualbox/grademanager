from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView
import pandas as pd
import io
from django.shortcuts import render


class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Student.objects.all()


class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Student.objects.all()


class Upload_marks(TemplateView):
    template_name = "upload_marks.html"

    def get_context_data(self, **kwargs):
        kwargs["csv"] = "csv"
        return kwargs

    def post(self, request):
        print(request)
        context = {"messages": []}

        csv = request.FILES["csv"]
        csv_data = pd.read_csv(io.StringIO(csv.read().decode("utf-8")))

        for record in csv_data.to_dict(orient="records"):
            try:
                Student.objects.create(
                    student_id=record["student_id"],
                    first_name=record["first_name"],
                    last_name=record["last_name"],
                    course_name=record["course_name"],
                    marks=record["marks"],
                )
            except Exception as e:
                context["exceptions_raised"] = e

        return render(request, self.template_name, context)


def mark_analysis(request):
    gradeF = Student.objects.filter(mark__gte=30, mark__lt=40).count()
    gradeP = Student.objects.filter(mark__gte=40, mark__lt=50).count()
    gradeC = Student.objects.filter(mark__gte=50, mark__lt=60).count()
    gradeB = Student.objects.filter(mark__gte=60, mark__lt=70).count()
    gradeA = Student.objects.filter(mark__gte=70, mark__lt=80).count()
    gradeAA = Student.objects.filter(mark__gte=80, mark__lte=100).count()
    
    print(gradeAA)
    gradesData = [gradeAA, gradeA, gradeB, gradeC, gradeP, gradeF]
    labels = ["AA(81-100)", "a", "b", "c", "p", "f"]
    
    context = {
        "gradesData": gradesData,
        "labels": labels,
    }
    print(context)
    return render(request, "index.html", context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

def students(request):
    form = StudentForm()

    if request.method == "POST":
        # Create student
        if "create" in request.POST:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("mark_analysis")

        # Delete student
        elif "delete" in request.POST:
            pk = request.POST.get("delete")
            student = get_object_or_404(Student, pk=pk)
            student.delete()
            return redirect("mark_analysis")

        # Update student
        elif "update" in request.POST:
            pk = request.POST.get("update")
            return redirect("student_update", pk=pk)

    # Retrieve all students
    students = Student.objects.all()

    context = {
        "students": students,
        "form": form,
    }

    return render(request, "students.html", context)