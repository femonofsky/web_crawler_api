from rest_framework import generics
from django_filters import rest_framework as filters
from crawler.models import CompanyProfile


class CompanyFilter(filters.FilterSet):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'security_code', 'email_address',
                  'country', 'phone', 'board', 'sector', 'sub_sector']