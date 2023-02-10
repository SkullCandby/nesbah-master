from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customer"
    )
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    permission = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.date_created)


class Employee(models.Model):
    # user = models.OneToOneField(
    #     User,
    #     null=True,
    #     blank=True,
    #     on_delete=models.CASCADE,
    #     related_name="employee"
    # )
    contact_person = models.CharField(max_length=200, null=True) #
    position = models.CharField(max_length=200, null=True) #
    mobile = models.CharField(max_length=200, null=True) #
    email = models.CharField(max_length=200, null=True) #

    regions = models.CharField(max_length=200, null=True) #
    years = models.CharField(max_length=200, null=True) #
    number_of_stuff = models.CharField(max_length=200, null=True) #
    avg_salary = models.CharField(max_length=200, null=True) #
    business_cap = models.CharField(max_length=200, null=True) #

    req_service = models.CharField(max_length=200, null=True) #
    sector = models.CharField(max_length=200, null=True) #
    saudi_stuff = models.CharField(max_length=200, null=True) #
    legal_form = models.CharField(max_length=200, null=True) #
    number_of_branches = models.CharField(max_length=200, null=True) #

    website = models.CharField(max_length=200, null=True) #
    notes = models.TextField(max_length=400, null=True) #

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    user_id = models.CharField(max_length=200, null=True) #
    company_name = models.CharField(max_length=200, null=True) #
    count_viewed = models.IntegerField(default=0, null=True)
    count_paid = models.IntegerField(default=0, null=True)
    def __str__(self):
        return str(self.date_created)

class Permissions(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="permission"
    )
    permission = models.CharField(max_length=200, null=True)

    def __dir__(self):
        return self.permission

