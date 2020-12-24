from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View

from home.forms import StudentForm
from home.models import Student

class StudentView(View):
    """This class displays a complete list of all students"""
    def get(self, request):
        """This function gets all the data info of the each
        student in the model and transfers it to the template"""
        students = Student.objects.all()
        return render(
            request=request,
            template_name='index.html',
            context={'Students': students, })


class CreateView (View):
    """This class allows you to create new students
    through a form and add their info to the database."""
    def get(self, request):
        """This function generates the form and transfers it to the template."""

        student_form = StudentForm()
        context = {"form": student_form, }
        return render(request, "form_index.html", context=context)

    def post(self, request):
        """This function gets data from a form and
        saves it to the table (in case if all the info
        is valid)."""
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()
        return redirect(reverse('students'))

class UpdateView(View):
    """This class allows you to update student's info
    through a form and add updated info to the database."""
    def get (self, request, id):
        """This function gets a date of the student under
        selected id, generates a form with the info
        of this student. User can update all the info in this form."""
        students = get_object_or_404(Student, id=id)
        student_form = StudentForm(instance=students)
        context = {"form": student_form, "student_id": students.id}
        return render(request, "update.html", context=context)

    def post (self, request, id):
        """This function gets updated data from a form and
        saves it to the table (in case if all the info
        is valid)."""
        students = get_object_or_404(Student, id=id)
        student_form = StudentForm(request.POST, instance=students)
        if student_form.is_valid():
            student_form.save()
        return redirect(reverse('students'))
