from django.shortcuts import render, redirect
from account.models import Employee, Customer, Permissions
from kinda_api import return_employees, return_employee, add_one, unlocked_applications
import json
from django.http import JsonResponse

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
            leads = return_employees(0, 0)
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
            context["leads"] = leads
        return render(request, 'bank.html', context)
    else:
        return redirect("/account/index")

def see_full_data(request):
    user = request.user
    print(user)
    permissions = Permissions.objects.get(user_id=user.id)
    print(permissions.permission)
    
    if permissions.permission == "admin":
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


