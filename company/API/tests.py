from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee

class EmployeeTests(APITestCase):

    def setUp(self):
        self.valid_payload = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'photo': 'http://example.com/john.jpg',
            'position': 'Software Engineer',
            'salary': 50000,
        }
        self.invalid_payload = {
            'first_name': '',
            'last_name': '',
            'date_of_birth': '',
            'photo': '',
            'position': '',
            'salary': -50000,
        }
        self.employee = Employee.objects.create(**self.valid_payload)

    def test_create_valid_employee(self):
        url = reverse('employee-list')
        response = self.client.post(url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(Employee.objects.get(id=2).first_name, 'John')

    def test_create_invalid_employee(self):
        url = reverse('employee-list')
        response = self.client.post(url, data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employee.objects.count(), 1)

    def test_retrieve_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')
        self.assertEqual(response.data['salary'], 50000)

    def test_update_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        payload = {
            'first_name': 'Jane',
            'salary': 60000,
        }
        response = self.client.patch(url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.first_name, 'Jane')
        self.assertEqual(self.employee.salary, 60000)

    def test_delete_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)
