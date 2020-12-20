from django.core.management import BaseCommand
from faker import Faker
from home.models import Student
class Command(BaseCommand):

    help = "Insert new students in the system"

    def add_arguments(self, parser):
        """This function is parsing all the arguments."""

        parser.add_argument("-l", "--len", type=int, default=10)

    def handle(self, *args, **options):

        """This function initializes Faker and
        generates information for the each field
        in the model "Student"."""

        faker = Faker()

        for _ in range(options['len']):
            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = faker.random_int(min=18, max=80)
            student.sex = faker.simple_profile()["sex"]
            student.address = faker.address()
            student.description = faker.text()
            student.birthday = faker.date_of_birth()
            student.email = faker.email()
            student.save()
