import csv

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View
from home.tasks import compile_task
from crispy_forms.utils import render_crispy_form
from home.filter import StudentFilter

from home.forms import StudentForm, SubjectForm, TeacherForm
from home.models import Student, Book, Subject, Teacher, Currency



class BookView(View):
    """Displays a complete list of all books"""
    def get (self, request):
        """Gets all the data info of the each
        book in the model and transfers it to the template"""
        books = Book.objects.all()
        return render(
            request=request,
            template_name='book_list.html',
            context={"books": books, "title" : "Books"} )

class BookDeleteView(View):
    """Delete book, that has been chosen by its id from template with books list"""
    def get (self, request, id):
        """Gets a date of the book under
        selected id."""
        book = get_object_or_404(Book, id=id)
        context = {"book": book, "title" : "Delete"}
        return render(request, "delete_book.html", context=context)

    def post (self, request, id):
        """Delete selected by id book from a Book model."""
        Book.objects.filter(id=id).delete()
        return redirect(reverse('book'))


class SubjectView(View):
    """Displays a complete list of all subjects"""
    def get (self, request):
        """Gets all the data info of the each
        subject in the model and transfers it to the template"""
        subjects = Subject.objects.all()

        return render(
            request=request,
            template_name='subject.html',
            context={"subjects": subjects, "title": "Subjects"} )


class SubjectUpdateView(View):
    """Allows you to update subject info
    through a form."""
    def get (self, request, id):
        """Gets a date of the subject under
        selected id, generates a form with the subject title."""
        subjects = get_object_or_404(Subject, id=id)
        students= Student.objects.filter(subject=None)
        subject_form = SubjectForm(instance=subjects)
        context = { "form": subject_form, "subjects": subjects, "students": students,
                   "title": "Subject update"}
        return render(request, "update_subject.html", context=context)

    def post (self, request, id):
        """Gets updated data from a form and
        saves it to the table (in case if all the info
        is valid)."""
        subjects = get_object_or_404(Subject, id=id)
        subject_form = SubjectForm(request.POST, instance=subjects)
        if subject_form.is_valid():
            subject_form.save()
        return redirect(reverse('subjects'))

class AddStudentView(View):
    """Add chosen by id student to the previously selected subject."""
    def get(self, request,  subject_id, student_id):
        """Get data info for the selected student and subject."""
        subject = get_object_or_404(Subject, id=subject_id)
        student= get_object_or_404(Teacher, id=student_id)
        context = {"student": student, "subject": subject, "title": "Add student"}
        return render(request, "add_student.html", context=context)

    def post (self, request,  subject_id, student_id):
        """Add selected subject to the data base of the student."""
        subject = get_object_or_404(Subject, id=subject_id)
        student = get_object_or_404(Student, id=student_id)
        subject.student.add(student)
        subject.save()
        return HttpResponseRedirect(reverse('update_subject', args=[subject_id]))


class DeleteSubjectView(View):
    """Delete chosen by id subject from student's data."""
    def get(self, request,  student_id, subject_id):
        """Get data info for the selected student and subject."""
        student = get_object_or_404(Student, id=student_id)
        subject= get_object_or_404(Subject, id=subject_id)
        context = {"student": student,"subject": subject, "title": "Update"}
        return render(request, "student_subject.html", context=context)

    def post (self, request,  student_id, subject_id ):
        """Remove subject from data of the chosen student."""
        student = get_object_or_404(Student, id=student_id)
        student.subject = None
        student.save()
        return HttpResponseRedirect(reverse('update_subject', args=[subject_id]))



class TeachersView(View):
    """Displays a complete list of all teachers"""
    def get (self, request):
        """Gets all the data info of the each
        teacher in the model and transfers it to the template"""
        teachers = Teacher.objects.all()

        return render(
            request=request,
            template_name='teacher.html',
            context={"teachers": teachers, "title" : "Teachers"} )

class TeacherUpdateView(View):
    """Allows you to update teacher info
    through a form."""
    def get (self, request, id):
        """Gets a date of the teacher under
        selected id, generates a form with the teacher name."""
        teacher = get_object_or_404(Teacher, id=id)
        students= Student.objects.filter().exclude(teacher__id=teacher.id)
        teacher_form = TeacherForm(instance=teacher)
        context = {"form": teacher_form, "students": students, "teacher": teacher, "title": "Teacher update"}
        return render(request, "update_teacher.html",  context=context)
    def post (self, request, id):
        """Gets updated data from a form and
        saves it to the table (in case if all the info
        is valid). Shows a link for the templates to add or delete student."""
        teacher = get_object_or_404(Teacher, id=id)
        teacher_form = TeacherForm(request.POST, instance=teacher)
        if teacher_form.is_valid():
            teacher_form.save()
        return redirect(reverse('teachers'))

class TeacherStudentView(View):
    """Add chosen by id student to the previously selected teacher."""
    def get(self, request,  teacher_id, student_id):
        """Get data info for the selected student and teacher."""
        teacher = get_object_or_404(Teacher, id=teacher_id)
        student= get_object_or_404(Student, id=student_id)
        context = {"student": student, "teacher": teacher, "title": "Add student"}
        return render(request, "teacher_student.html", context=context)

    def post (self, request,  teacher_id, student_id):
        """Add selected student to the data base of the teacher."""
        teacher = get_object_or_404(Teacher, id=teacher_id)
        student= get_object_or_404(Student, id=student_id)
        teacher.students.add(student)
        teacher.save()
        return HttpResponseRedirect(reverse('update_teacher', args=[teacher_id]))

class TeacherDeleteView(View):
    """Delete chosen by id student from teacher's data."""
    def get(self, request,  student_id, teacher_id):
        """Get data info for the selected student and teacher."""
        student = get_object_or_404(Student, id=student_id)
        teacher= get_object_or_404(Teacher, id=teacher_id)
        context = {"student": student, "teacher": teacher, "title": "Delete teacher"}
        return render(request, "delete_teacher.html", context=context)

    def post (self, request,  student_id, teacher_id):
        """Remove student from data of the chosen teacher."""
        teacher = get_object_or_404(Teacher, id=teacher_id)
        student = get_object_or_404(Student, id=student_id)
        teacher.students.remove(student)
        return HttpResponseRedirect(reverse('update_teacher', args=[teacher_id]))


class StudentView(View):
    """Displays a complete list of all students"""
    def get(self, request):
        """Gets all the data info of the each
        student in the model and transfers it to the template"""
        compile_task.delay()
        students = Student.objects.all()
        myFilter = StudentFilter(request.GET, queryset= students)
        students = myFilter.qs
        return render(
            request=request,
            template_name='index.html',
            context={"students": students, "title" : "Students", "myFilter": myFilter} )


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
        student_form = StudentForm(request.POST, instance=students)
        if student_form.is_valid():
            student_form.save()
        return redirect(reverse('students'))


class CurrencyView(View):
    """Displays currency list"""
    def get(self, request):
        """Gets all the data info of currency
        in the model and transfers it to the template"""
        # compile_task.delay()
        currencies = Currency.objects.all()
        return render(
            request=request,
            template_name='currency.html',
            context={"currencies": currencies, "title" : "Currency"} )

class CSVView(View):

    def get(self, request):
        response = HttpResponse(content_type="text/csv")

        response['Content-Disposition'] = "attachment; filename=all_students.csv"

        writer_for_response = csv.writer(response)
        writer_for_response.writerow(["ID", "Name", "Surname", "Age", "Sex", "Address",
                                      "Birthday", "Email", "Social Url", "Book", "Subject",])

        students = Student.objects.all()
        for student in students:
            writer_for_response.writerow([
                student.id,
                student.name,
                student.surname,
                student.age,
                student.sex,
                student.address,
                student.birthday,
                student.email,
                student.social_url if student.book else None,
                student.book.title if student.book else None,
                student.subject.title if student.subject else None,
            ])
        return response

class JsonView(View):

    def get(self, request):
        students = Student.objects.all()
        return JsonResponse({
            "students": list(students.values(
                "id",
                "name",
                "surname",
                "age",
                "sex",
                "address",
                "birthday",
                "email",
                "social_url",
                "book__title",
                "subject__title",
            )),
        })

