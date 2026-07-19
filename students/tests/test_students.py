from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from students.models import Student

class StudentAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="ram",
            password="123456"
        )

        Student.objects.create(
            name="Ram",
            email="ram@gmail.com",
            age=22
        )

    def test_get_students(self):
        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.get(
            "/api/students/modelviewset/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data["results"]),
            1
        )