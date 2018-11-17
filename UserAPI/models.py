from django.db import models
from django.db.models import CharField, IntegerField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Authentication user model
# User Type Choice
BANK = "Bank"
MEDI = "HealthCare"
SCHOOL = "Education"
RETAIL = "RetailStores"
MISC = "Others"

COMPANY_TYPES = ((BANK, "Bank"), (MEDI, "HealthCare"), (SCHOOL, "Education"), (RETAIL, "RetailStores"), (MISC, "Others"))

class User(models.Model):
    displayName = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    uid = models.CharField(max_length=200, default='defaultuid', unique=True)
    company_type = models.CharField(max_length=10, choices=COMPANY_TYPES, null=False)
    primary_color = models.CharField(max_length=10)
    secondary_color = models.CharField(max_length=10)

    def __str__(self):
        return '{} - {} - {}'.format(self.email, self.company_name, self.company_type)
