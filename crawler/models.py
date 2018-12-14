import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField,JSONField
from django.contrib.postgres.fields.jsonb import JSONField as JSONBField
# Create your models here.
class CompanyProfile(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    company_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    security_code = models.CharField(max_length=155, unique=True, null=False, blank=False)
    office_address = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.EmailField(max_length=155, null=True, blank=True)
    country = models.CharField(max_length=255, default= "Indonesia")
    phone = models.CharField(max_length=100, null=True, blank=True)
    fax = ArrayField(models.CharField(max_length=100, default=[], blank=True, null=True))
    npwp = models.CharField(max_length=100, null=True, blank=True)
    company_website = models.CharField(max_length=255, null=True, blank=True)
    ipo_date = models.DateField(max_length=255, null=True, blank=True)
    board = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=150, null=True, blank=True)
    sub_sector = models.CharField(max_length=150, null=True, blank=True)
    registrar = models.CharField(max_length=255, null=True, blank=True)
    corporate_Secretary = JSONBField(default=list,null=True,blank=True)
    director = JSONBField(default=list,null=True,blank=True)

    def __str__(self):
        return self.company_name