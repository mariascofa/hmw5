from django.forms import ModelForm
from home.models import Student

class StudentForm(ModelForm):
    """Data base info"""
    class Meta:
        model = Student
        fields = ["name", "surname", "age", "sex", "address",
                  "description", "birthday", "email", "social_url"]

