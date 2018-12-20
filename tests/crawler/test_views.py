
from django.test import TestCase
from django.urls import reverse
# from django.test import Client
from rest_framework import status


class CompanyViewTest(TestCase):
    def setUp(self):
        pass

    def test_create_company(self):
        url = reverse('create_company')
        data = {
            'company_name': "Astra Agro Lestari Tbk",
            'security_code': "AALI",
            'office_address': "Jl Pulo Ayang Raya Blok OR No. 1 Kawasan Industri Pulogadung Jakarta",
            'email_address': "Investor@astra-agro.co.id",
            'phone': "+62 461-65-55",
            'fax': ["+62 461-6655", "+62 461-6677", "+62 461-6688"],
            'npwp': "01.334.427.0-054.000",
            'company_website': "http://www.astra-agro.co.id",
            'ipo_date': "1997-12-09",
            'board': "UTAMA",
            'sector': "AGRICULTURE",
            'sub_sector': "PLANTATION",
            'registrar': "",
            'corporate_Secretary': [],
            'director': [],
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data

    def test_get_all_companies(self):
        self.test_create_company()
        url = reverse('all_companies')
        response = self.client.get(url)
        data = response.data['data']
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_companies_by_filtering(self):
        self.test_create_company()
        url = reverse('all_companies')
        url = url+"?company_name=WRONG_COMPANY_NAME"
        response = self.client.get(url)
        data = response.data['data']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 0)
