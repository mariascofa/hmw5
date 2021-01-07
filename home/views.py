from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View
from home.tasks import compile_task
from crispy_forms.utils import render_crispy_form


from home.forms import StudentForm
from home.models import Student

class StudentView(View):
    """Displays a complete list of all students"""
    def get(self, request):
        """Gets all the data info of the each
        student in the model and transfers it to the template"""
        compile_task.delay()
        students = Student.objects.all()
        return render(
            request=request,
            template_name='index.html',
            context={"students": students, "title" : "Students"} )


class CreateView (View):
    """Allows you to create new students
    through a form and add their info to the database."""
    def get(self, request):
        """Generates the form and transfers it to the template."""

        student_form = StudentForm()
        context = {"form": student_form, "title" : "Create" }
        return render(request, "form_index.html", context=context)

    def post(self, request):
        """Gets data from a form and
        saves it to the table (in case if all the info
        is valid)."""
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()
        return redirect(reverse('students'))

class UpdateView(View):
    """Allows you to update student's info
    through a form and add updated info to the database."""
    def get (self, request, id):
        """Gets a date of the student under
        selected id, generates a form with the info
        of this student. User can update all the info in this form."""
        students = get_object_or_404(Student, id=id)
        student_form = StudentForm(instance=students)
        context = {"form": student_form, "student": students, "title" : "Update"}
        return render(request, "update.html", context=context)

    def post (self, request, id):
        """Gets updated data from a form and
        saves it to the table (in case if all the info
        is valid)."""
        students = get_object_or_404(Student, id=id)
        # ctx = {}
        # ctx.update(csrf(request))
        student_form = StudentForm(request.POST, instance=students)
        # form_html = render_crispy_form(student_form, context=ctx)
        if student_form.is_valid():
            student_form .save()
        return redirect(reverse('students'))
