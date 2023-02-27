from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Company, Employee
from rest_framework.test import APITestCase


class CompanyAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.valid_company_data = {
            "name": "Adiiidas",
            "logo": "",
            "description": "this is the adidas company welco",
        }

        self.invalid_company_data = {
            "logo": "https://example.com/logo.png",
            "description": "a sa aaaaaa"
        }

    def test_create_valid_company(self):
        response = self.client.post(
            reverse('company-list'),
            data=self.valid_company_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_company(self):
        response = self.client.post(
            reverse('company-list'),
            data=self.invalid_company_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_company(self):
        company = Company.objects.create(
            name="nike",
            logo="https://example.com/logo.png",
            description="nike is a great company"
        )
        response = self.client.get(reverse('company-detail', args=[company.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_company(self):
        company = Company.objects.create(
            name="puma",
            logo="https://example.com/logo.png",
            description="puma is a great company"
        )
        response = self.client.put(
            reverse('company-detail', args=[company.id]),
            data={
                "name": "rebook",
                "logo": "https://example.com/logo.png",
                "description": "rebook is a great company"
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_company(self):
        company = Company.objects.create(
            name="nike",
            logo="https://example.com/logo.png",
            description="nike is a company"
        )
        response = self.client.delete(reverse('company-detail', args=[company.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class EmployeeTests(TestCase):

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