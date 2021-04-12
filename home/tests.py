import freezegun
from django.forms import model_to_dict
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from home.models import Teacher, Student, Subject, Book

@freezegun.freeze_time('2021-04-02')
class TeacherApiTests(APITestCase):
    """Tests on creating, reading, updating and deleting objects from Teacher's model."""
    def setUp(self):
        self.first_teacher = Teacher.objects.create(name= "Bill Smith")
        self.teachers = Teacher.objects.all()


    def test_create_teacher(self):
        """Test for creating new teacher."""
        response=self.client.post(
            reverse("teachers-list",),
        data={"name":"John Smith"})

        teacher = Teacher.objects.last()
        self.assertEqual(response.json(),
                         {'created_at': '2021-04-02T00:00:00Z', 'name': 'John Smith', 'updated_at': '2021-04-02T00:00:00Z'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(teacher.name, "John Smith")
        self.assertEqual(self.teachers.count(), 2)


    def test_read_teacher(self):
        """Test for getting json-data from Teacher's model."""
        response=self.client.get(
            reverse('teachers-list',))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(),   {'count': 0, 'next': None, 'previous': None, 'results': []})


    def test_update_teacher(self):
        """Test on updating info for chosen by id teacher."""
        response=self.client.put(
            reverse('teachers-detail', kwargs={'pk': self.first_teacher.pk}),
            {"name":"Will Smith"})

        self.first_teacher.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.first_teacher.name, "Will Smith")

        self.assertEqual(response.json(),
                         {'created_at': '2021-04-02T00:00:00Z', 'name': 'Will Smith',
                          'updated_at': '2021-04-02T00:00:00Z'})

    def test_delete_teacher(self):
        """Test for deleting teacher from Teacher's model."""
        response=self.client.delete(
            reverse('teachers-detail', kwargs={'pk': self.first_teacher.pk}))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.teachers.count(), 0)

@freezegun.freeze_time('2021-04-02')
class StudentApiTests(APITestCase):
    """Tests on creating, reading, updating and deleting objects from Student's model."""
    def setUp(self):
        self.first_student = Student.objects.create(name= "Dana", surname= "Stone")
        self.students = Student.objects.all()

    def test_create_student(self):
        """Test for creating new student."""
        response=self.client.post(
            reverse("students-list",),
        data={"name":"Sara", "surname": "White"})


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        student = Student.objects.last()
        self.assertEqual((student.name, student.surname),("Sara", "White"))
        self.assertEqual(self.students.count(), 2)
        self.assertEqual(response.json(),
                         {'book': 1,'created_at': '2021-04-02T00:00:00Z','updated_at': '2021-04-02T00:00:00Z',
                          "name":"Sara", "surname": "White"})

    def test_read_student(self):
        """Test for getting json-data from Student's model."""
        response=self.client.get(
            reverse('students-list',))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(),   {'count': 0, 'next': None, 'previous': None, 'results': []})


    def test_update_student(self):
        """Test on updating info for chosen by id student."""
        response=self.client.put(
            reverse('students-detail', kwargs={'pk': self.first_student.pk}),
            {"name":"Lara", "surname": "Willson" })

        self.first_student.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual((self.first_student.name, self.first_student.surname),("Lara", "Willson"))
        self.assertEqual(response.json(),
                         {'book': None,'created_at': '2021-04-02T00:00:00Z', 'updated_at': '2021-04-02T00:00:00Z',
                          "name": "Lara", "surname": "Willson"})

    def test_delete_student(self):
        """Test for deleting student from Student's model."""
        response=self.client.delete(
            reverse('students-detail', kwargs={'pk': self.first_student.pk}))


        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.students.count(), 0)

@freezegun.freeze_time('2021-04-02')
class SubjectApiTests(APITestCase):
    """Tests on creating, reading, updating and deleting objects from Subject's model."""
    def setUp(self):
        self.first_subject = Subject.objects.create(title= "Python")
        self.subjects = Subject.objects.all()

    def test_create_subject(self):
        """Test for creating new subject."""
        response=self.client.post(
            reverse("subjects-list",),
        data={"title":"Java"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        subject = Subject.objects.last()
        self.assertEqual(subject.title, "Java")
        self.assertEqual(self.subjects.count(), 2)
        self.assertEqual(response.json(),
                         {'created_at': '2021-04-02T00:00:00Z', 'updated_at': '2021-04-02T00:00:00Z',
                          "title":"Java"})

    def test_read_subject(self):
        """Test for getting json-data from Subject's model."""
        response=self.client.get(
            reverse('subjects-list',))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(),   {'count': 0, 'next': None, 'previous': None, 'results': []})


    def test_update_subject(self):
        """Test on updating info for chosen by id subject."""
        response=self.client.put(
            reverse('subjects-detail', kwargs={'pk': self.first_subject.pk}),
            {"title":"PHP"})

        self.first_subject.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.first_subject.title, "PHP")
        self.assertEqual(response.json(),
                         {'created_at': '2021-04-02T00:00:00Z', 'updated_at': '2021-04-02T00:00:00Z',
                          "title": "PHP"})

    def test_delete_subject(self):
        """Test for deleting subject from Subject's model."""
        response=self.client.delete(
            reverse('subjects-detail', kwargs={'pk': self.first_subject.pk}))


        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.subjects.count(), 0)

@freezegun.freeze_time('2021-04-02')
class BookApiTests(APITestCase):
    """Tests on creating, reading, updating and deleting objects from Book's model."""
    def setUp(self):
        self.first_book = Book.objects.create(title= "qwe098")
        self.books = Book.objects.all()

    def test_create_book(self):
        """Test for creating new book."""
        response=self.client.post(
            reverse("books-list",),
        data={"title":"tyu456"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        book = Book.objects.last()
        self.assertEqual(book.title, "tyu456")
        self.assertEqual(self.books.count(), 2)
        self.assertEqual(response.json(),
                         {'created_at': '2021-04-02T00:00:00Z', 'updated_at': '2021-04-02T00:00:00Z',
                          "title": "tyu456"})

    def test_read_book(self):
        """Test for getting json-data from Book's model."""
        response=self.client.get(
            reverse('books-list',))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(),   {'count': 0, 'next': None, 'previous': None, 'results': []})

    def test_update_book(self):
        """Test on updating info for chosen by id book."""
        response=self.client.put(
            reverse('books-detail', kwargs={'pk': self.first_book.pk}),
            {"title":"sdf678"})

        self.first_book.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.first_book.title, "sdf678")
        self.assertEqual(response.json(),
                         {'created_at': '2021-04-02T00:00:00Z', 'updated_at': '2021-04-02T00:00:00Z',
                          "title": "sdf678"})

    def test_delete_book(self):
        """Test for deleting book from Book's model."""
        response=self.client.delete(
            reverse('books-detail', kwargs={'pk': self.first_book.pk}))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.books.count(), 0)






