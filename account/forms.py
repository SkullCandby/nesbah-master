from django.forms import ModelForm, Select
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Customer, Employee


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'email',
                  'password1',
                  'password2',
                  ]


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'regions': Select(choices=[
                (1, 'One'),
                (2, 'Two'),
                (3, 'Three')
            ]),
            'req_service': Select(choices=[
                (1, 'One'),
                (2, 'Two'),
                (3, 'Three')
            ]),
            'sector': Select(choices=[
                (1, 'One'),
                (2, 'Two'),
                (3, 'Three')
            ]),
            'number_of_stuff': Select(choices=[
                (1, 'One'),
                (2, 'Two'),
                (3, 'Three')
            ]),
            'legal_form': Select(choices=[
                (1, 'One'),
                (2, 'Two'),
                (3, 'Three')
            ]),
            'business_cap': Select(choices=[
                (1, 'One'),
                (2, 'Two'),
                (3, 'Three')
            ]),


        }
        exclude = ['user']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
