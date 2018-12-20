import factory
from django.test import TestCase
from crawler.models import CompanyProfile


class CompanyProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = CompanyProfile
        django_get_or_create = ()
    company_name = "Astra Agro Lestari Tbk"
    security_code = "AALI"
    office_address = "Jl Pulo Ayang Raya Blok OR No. 1 Kawasan Industri Pulogadung Jakarta"
    email_address = "Investor@astra-agro.co.id."
    phone = "+62 461-65-55"
    fax = ["+62 461-6655", "+62 461-6677", "+62 461-6688"]
    npwp = "01.334.427.0-054.000"
    company_website = "http://www.astra-agro.co.id"
    ipo_date = "1997-12-09"
    board = "UTAMA"
    sector = "AGRICULTURE"
    sub_sector = "PLANTATION"
    registrar = "PT. Raya Saham Registrar (dulu bernama PT. Risjad Salim Registra"
    corporate_Secretary = [{'name': 'Mario Casimirus Surung Gultom',
                            'email': 'investor@astra-agro.co.id', 'phone': '+62 021-4616555'}]
    director = [{"name": "Santosa", "position": "PRESIDEN DIREKTUR"},
                {"name": "Joko Supriyono", "position": "WAKIL PRESIDEN DIREKTUR"}]


class TestCompanyProfileFactory(TestCase):
    def setUp(self):
        self.company_profile = CompanyProfileFactory.create()

    def test_unicode(self):
        self.assertEqual(str(self.company_profile), self.company_profile.company_name)

    def test_country_default(self):
        self.assertEqual(self.company_profile.country, "Indonesia")

    def test_security_code(self):
        self.assertEqual(self.company_profile.security_code, "AALI")

    def test_sector(self):
        self.assertEqual(self.company_profile.sector, "AGRICULTURE")
