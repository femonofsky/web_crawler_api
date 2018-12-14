from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from crawler.serializers import *
from crawler.models import *
from crawler.filters import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as filters

from rest_framework_tracking.mixins import LoggingMixin

# Create your views here.
class GetAllCompanies(LoggingMixin, ListAPIView):
    """
    Get all companies
    """
    serializer_class = CompanySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CompanyFilter

    def get(self, request, *args, **kwargs):
        company_profiles = CompanyProfile.objects.all()
        serializer = self.serializer_class(instance=company_profiles, many=True)
        return format_response(
            status.HTTP_201_CREATED,
            serializer.data,
            'Successful'
        )

class CreateCompany(LoggingMixin, CreateAPIView):
    """
        Create company
    """
    serializer_class = CompanySerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
        except ValidationError as error:
            return format_error_response(status.HTTP_400_BAD_REQUEST, error.detail)
        else:
            serializer.save()
        return format_response(
            status.HTTP_201_CREATED,
            serializer.data,
            'Company Created.'
        )

def format_response(code, data, msg):
    response = Response({
        'status_code': code,
        'message': msg,
        'data': data
    }, status=code)

    return response

def format_error_response(code, msg):
    response = Response({
        'code': code,
        'message': msg
    }, status=code)

    return response


