import uuid

from django.core.paginator import Paginator
from rest_framework import serializers

import home
from home.models import Student, Subject, Teacher, Book


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["title"]

class TeacherSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField("paginated_students")

    def paginated_students(self,obj):
        students = Student.objects.all()

        pagination = Paginator(students, per_page=2)
        pagination_students = pagination.page(1)

        return StudentSerializer(instance=pagination_students,many=True).data

    class Meta:
        model = Teacher
        fields = ["name", "students"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "surname", "age", "sex", "book"]
        read_only_fields = ('book',)

