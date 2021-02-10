"""hmw5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import StudentView, CreateView, UpdateView, BookView, SubjectView, TeachersView, BookDeleteView, \
    SubjectUpdateView, DeleteSubjectView, TeacherUpdateView, TeacherDeleteView, AddStudentView, TeacherStudentView,\
    CurrencyView



urlpatterns = [
    path('currency/', CurrencyView.as_view(), name='currency'),
    path('admin/', admin.site.urls),
    path('subjects/', SubjectView.as_view(), name='subjects'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('', StudentView.as_view(), name='students'),
    path("students/create/", CreateView.as_view(), name='create'),
    path("students/update/<id>/", UpdateView.as_view(), name="update"),
    path("books/", BookView.as_view(), name="book"),
    path("books/delete/<id>/", BookDeleteView.as_view(), name="delete_book"),
    path("subjects/update/<id>/", SubjectUpdateView.as_view(), name="update_subject"),
    path("subjects/delete/<subject_id>/<student_id>/", DeleteSubjectView.as_view(), name="student_subject"),
    path("teachers/update/<id>/", TeacherUpdateView.as_view(), name="update_teacher"),
    path("teachers/delete/<student_id>/<teacher_id>/", TeacherDeleteView.as_view(), name="delete_teacher"),
    path("subjects/update/<subject_id>/<student_id>/", AddStudentView.as_view(), name="add_student"),
    path("teacher/update/<teacher_id>/<student_id>/", TeacherStudentView.as_view(), name="teacher_student"),
]

