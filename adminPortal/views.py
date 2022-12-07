from django.shortcuts import render

from account.models import Employee, Customer
from kinda_api import past_week_users, past_week_employee


# Create your views here.
def main(request):
    user = request.user
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
    return render(request, 'adminPortal.html', context)
