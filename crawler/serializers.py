from rest_framework import serializers

from crawler.models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'
