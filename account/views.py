from email.mime.text import MIMEText

from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template.defaulttags import url
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ResetPassword
from .models import Permissions
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
# Create your views here.
from datetime import datetime, timedelta
from kinda_api import past_week_users, past_week_employee
def index(request):
    context = {}
    user = request.user
    print(user)
    if user.is_active:
        context = {'name': user.first_name,
                   'name_input': user.first_name}
        return render(request, 'homepage.html', context)
    else:

        context = {'name': 'Sign in',
                   'name_input': ""}
        return render(request, 'index.html', context)

def login_page(request):
    user = request.user
    if not user.is_active:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                user = request.user

                try:
                    permissions = Permissions.objects.get(user_id=user.id)
                    if permissions.permission == "admin":
                        return redirect("adminportal")
                    elif permissions.permission == "bankuser":
                        print("yep")
                        return redirect("bankportal")
                    else:
                        return redirect('home')
                except:
                    return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
    else:
        logout(request)
        return HttpResponse('profile page')
    context = {}
    return render(request, 'login1.html', context)

def logout_user(request):
    logout(request)
    return redirect("/account/index/")

def register_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('activate.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(
                mail_subject,  message, to=[to_email]
            )
            # email.attach_alternative(html, "text/html")
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = CreateUserForm()
    return render(request, 'register1.html', {'form': form})

def activate(request, uidb64, token):
    print(request.path)
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        customer = Customer(user=user)
        customer.email = user.email
        customer.name = user.first_name
        customer.save()

        permission = Permissions(user=user)
        permission.permission = "employee"
        permission.save()

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



def employee(request):
    form = EmployeeForm()
    context = {'form': form}
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()

    else:
        print(past_week_users(Customer))
        print(past_week_employee(Employee))
    return render(request, 'homepage_2.html', context)


def deposit(request):
    context = {}
    return render(request, 'fixed_deposit.html', context)


def whyUs(request):
    context = {}
    return render(request, 'why_us.html', context)

def credit(request):
    context = {}
    return render(request, 'credit_card.html', context)

def reset(request):
    if request.method == "POST":
        form = GetUserName(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            current_site = get_current_site(request)
            mail_subject = 'Reset password link has been sent to your email id'
            message = render_to_string('reset.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user.email
            email = EmailMultiAlternatives(
                mail_subject, message, to=[to_email]
            )
            # email.attach_alternative(html, "text/html")
            email.send()
            return HttpResponse('Please check your email to reset the password')

    else:
        form = GetUserName()
    context = {"form": form}
    return render(request, 'forget.html', context)
def resetPassword(request,  uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if request.method == "POST":
        form = ResetPassword(request.POST)

        print(form)
        if form.is_valid():
            print(form.cleaned_data['password1'])
            print(form.cleaned_data['password2'])
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user.set_password(form.cleaned_data['password1'])
                user.save()
                return redirect('/account/login/')
        else:
            messages.info(request, 'Passwords are different')
    else:
        form = ResetPassword()
    context = {'form': form}
    return render(request, 'resetPassword.html', context)

