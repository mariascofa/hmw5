from rest_framework import serializers

from home.models import Student, Subject, Teacher, Book


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "surname", "age", "sex"]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["title"]

class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ["name", "students"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title"]