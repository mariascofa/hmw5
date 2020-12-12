from django.http import HttpResponse
from django.shortcuts import render
from home.models import Student


def show_all_students(request):
    """This function will return all the students from the
     model in the template."""
    students = Student.objects.all()
    return render(
        request=request,
        template_name='index.html',
        context={
            'Students': students,
        }
    )


