from django.shortcuts import render, redirect
from account.models import Employee, Customer, Permissions
from kinda_api import return_employees, return_employee, add_one, unlocked_applications, all_bank, count_view
import json
from django.http import JsonResponse, HttpResponse

# Create your views here.
def main(request):
    user = request.user
    print(user)
    permissions = Permissions.objects.get(user_id=user.id)
    print(permissions.permission)
    context = {}
    print(all_bank())
    if permissions.permission == "bankuser" or permissions.permission == "admin":
        context = {}
        if request.method == "POST":
            print(request.POST)
        if request.method == "GET":
            leads = return_employees(0, 0)
            unlocked = unlocked_applications(user)
            hide_fields = ["contact_person", "position", "mobile", "email", "website", "notes"]

            for lead in leads:
                for field in hide_fields:
                    lead[field] = "*"
                lead["date_created"] = str(lead["date_created"])

            """
            So both all of the data you receive in this format: 
            'users': {'Tue': 1} 
            'leads': {'Mon': 4, 'Sun': 1, 'Sat': 2}
            """
            context["username"] = user
            context["role"] = permissions.permission
            context["leads"] = leads
            context["unlocked"] = unlocked
        return render(request, 'bank.html', context)
    else:
        return redirect("/account/index")

def history(request):
    user = request.user
    print(user)
    permissions = Permissions.objects.get(user_id=user.id)
    print(permissions.permission)

    context = {}
    if permissions.permission == "bankuser" or permissions.permission == "admin":
        context = {}
        if request.method == "GET":
            leads = return_employees(0, 0)
            unlocked = unlocked_applications(user)
            leads_to_return = []
            
            for lead in leads:
                if str(lead["id"]) in unlocked:
                    lead["date_created"] = str(lead["date_created"])
                    leads_to_return.append(lead)
                
            """
            So both all of the data you receive in this format: 
            'users': {'Tue': 1} 
            'leads': {'Mon': 4, 'Sun': 1, 'Sat': 2}
            """
            context["leads"] = leads_to_return
            context["leadsamount"] = len(leads)
            context["username"] = user
            context["role"] = permissions.permission
        return render(request, 'history.html', context)
    else:
        return redirect("/account/index")

def see_full_data(request):
    user = request.user
    print(user)
    permissions = Permissions.objects.get(user_id=user.id)
    print(permissions.permission)
    
    if permissions.permission == "bankuser" or permissions.permission == "admin":
        if request.method == "POST":
            json_data = json.loads(request.body)
            print(json_data)
            """
            TODO:
            Here, save the data that this bank user requested to see full data
            """
            add_one(user, json_data['application_id'])
            lst = unlocked_applications(user)
            print(lst)

            return JsonResponse(return_employee(json_data["application_id"]), safe=False)

    return redirect("/bank/portal")


def application_viewed(request):
    user = request.user
    permissions = Permissions.objects.get(user_id=user.id)

    if permissions.permission == "bankuser" or permissions.permission == "admin":
        if request.method == "POST":
            json_data = json.loads(request.body)
            print(json_data)
            if json_data["view_application"] is not None:
                count_view(request.user)
    return redirect("/bank/portal")


