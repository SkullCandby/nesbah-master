from django.shortcuts import render, redirect

from account.models import Employee, Customer, Permissions
from kinda_api import past_week_users, past_week_employee


# Create your views here.
def main(request):
    user = request.user
    print(user)
    permissions = Permissions.objects.get(user_id=user.id)
    print(permissions.permission)
    context = {}
    if permissions.permission == "admin":
        context = {}
        if request.method == "GET":
            users_for_the_week = past_week_users(Customer)
            employees_for_the_week = past_week_employee(Employee)
            """
            So both all of the data you receive in this format: 
            'users': {'Tue': 1} 
            'leads': {'Mon': 4, 'Sun': 1, 'Sat': 2}
            """
            context['users'] = users_for_the_week
            context['leads'] = employees_for_the_week
            print(context)
        return render(request, 'admin-portal.html', context)
    else:
        return redirect("/account/index")


def leads(request):
    user = request.user
    print(user)
    permissions = Permissions.objects.get(user_id=user.id)
    print(permissions.permission)
    context = {}
    if permissions.permission == "admin":
        context = {}
        if request.method == "GET":
            users_for_the_week = past_week_users(Customer)
            employees_for_the_week = past_week_employee(Employee)
            """
            So both all of the data you receive in this format: 
            'users': {'Tue': 1} 
            'leads': {'Mon': 4, 'Sun': 1, 'Sat': 2}
            """
            context['users'] = users_for_the_week
            context['leads'] = employees_for_the_week
            print(context)
        return render(request, 'leads.html', context)
    else:
        return redirect("/account/index")

def users(request):
    user = request.user
    print(user)
    permissions = Permissions.objects.get(user_id=user.id)
    print(permissions.permission)
    context = {}
    if permissions.permission == "admin":
        context = {}
        return render(request, 'user.html', context)
    else:
        return redirect("/account/index")
