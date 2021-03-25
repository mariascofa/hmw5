import django_filters

from home.models import Student

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ("name", "teacher__name")
