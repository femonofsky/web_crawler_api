from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from crawler.serializers import *
from crawler.models import *
from crawler.filters import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class GetAllCompanies(ListAPIView):
    """
    Get all companies
    """
    serializer_class = CompanySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompanyFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return format_response(
                status.HTTP_200_OK,
                serializer.data,
                'Successful'
        )

    def get_queryset(self):
        return CompanyProfile.objects.all()


class CreateCompany(CreateAPIView):
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


