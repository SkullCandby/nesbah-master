from django.core.exceptions import ValidationError
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
class ResetPassword(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), min_length=9)
    password2 = forms.CharField(widget=forms.PasswordInput(), min_length=9)

    class Meta:
        model = User
        fields = ('password1', 'password2')
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

class GetUserName(forms.Form):
    username = forms.CharField(max_length=50)
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
                (1, 'Eastern'),
                (2, 'Western'),
                (3, 'Southern'),
                (4, 'Northern')
            ]),
            'req_service': Select(choices=[
                (1, 'Company Enrollment & Staff Offering'),
                (2, 'Company Financing Services'),
                (3, 'Account Opening'),
                (4, 'Offering Discount to Banking Customers')
            ]),
            'sector': Select(choices=[
                (1, 'Private'),
                (2, 'Government'),
                (3, 'Semi Government')
            ]),
            # 'number_of_stuff': Select(choices=[
            #     (1, 'One'),
            #     (2, 'Two'),
            #     (3, 'Three')
            # ]),
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
