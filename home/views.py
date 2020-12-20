from django.shortcuts import render, redirect
from home.forms import StudentForm
from home.models import Student


def show_all_students(request):

    students = Student.objects.all()
    return render(
        request=request,
        template_name='index.html',
        context={'Students': students, })

def create_students(request):

    if request.method == "GET":
        student_form = StudentForm()
        context = {"form": student_form, }
        return render(request, "form_index.html", context=context)
    
    elif request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
        return redirect('/students')
