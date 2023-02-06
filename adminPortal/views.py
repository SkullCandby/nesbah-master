from django.shortcuts import render, redirect

from account.models import Employee, Customer, Permissions
from kinda_api import past_week_users, past_week_employee, return_employees, all_unlocked_applications


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
            leads = return_employees(0, 0)
            lead_ids = []
            """
            So both all of the data you receive in this format: 
            'users': {'Tue': 1} 
            'leads': {'Mon': 4, 'Sun': 1, 'Sat': 2}
            """

            for lead in leads:
                lead_ids.append(lead["id"])

            context['users'] = users_for_the_week
            context['leads'] = employees_for_the_week
            context['leadids'] = lead_ids
            context['allunlockedleads'] = all_unlocked_applications()

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
            leads = return_employees(0, 0)
            for lead in leads:
                lead["date_created"] = str(lead["date_created"])
            """
            So both all of the data you receive in this format: 

            {'leads': [{'id': 4, 'user_id': None, 'contact_person': 'Gleb Meshkov', 'position': 'dwad', 
            'mobile': '0625204125', 'email': 'gdmeshkov@gmail.com', 'regions': '1', 'years': '13', 
            'number_of_stuff': '1', 'avg_salary': '11111', 'business_cap': '1', 'req_service': '1', 
            'sector': '1', 'saudi_stuff': '1244', 'legal_form': '1', 'number_of_branches': '2', 
            'website': 'weweewewe', 'notes': 'adawdwdad', 'date_created': '2022-12-05 12:20:03.212047+00:00'}]
            """
            context['leads'] = leads
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
