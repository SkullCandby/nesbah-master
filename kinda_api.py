from datetime import datetime, timedelta

from account.models import Employee


# import pandas as pd
from bankPortal.models import bank_portal_new


def past_week_employee(data):
    one_week_ago = datetime.today() - timedelta(days=7)
    data = data.objects.filter(date_created__gte=one_week_ago).all()
    dd_weekdays = {
        1: 'Mon',
        2: 'Tue',
        3: 'Wed',
        4: 'Thur',
        5: 'Fri',
        6: 'Sat',
        7: 'Sun'
    }
    dd = {}
    for i in range(len(data)):
        datetime_object = datetime.strptime(str(data[i]).split()[0], '%Y-%m-%d')
        weekday_name = dd_weekdays[datetime_object.weekday() + 1]
        try:
                dd[weekday_name] += 1
        except:
                dd[weekday_name] = 1
    return dd

def past_week_users(data):
    one_week_ago = datetime.today() - timedelta(days=7)
    data = data.objects.filter(date_created__gte=one_week_ago).all()
    dd_weekdays = {
        1: 'Mon',
        2: 'Tue',
        3: 'Wed',
        4: 'Thur',
        5: 'Fri',
        6: 'Sat',
        7: 'Sun'
    }
    dd = {}
    for i in range(len(data)):
        datetime_object = datetime.strptime(str(data[i]).split()[0], '%Y-%m-%d')
        weekday_name = dd_weekdays[datetime_object.weekday() + 1]
        try:
                dd[weekday_name] += 1
        except:
                dd[weekday_name] = 1

    return dd

def return_employees(min_stuff, min_avg_salary):
    filtered_rows = list(Employee.objects.all().values())
    new_arr = []
    blured_arr = []
    for i in range(len(filtered_rows)):
        try:
            if int(filtered_rows[i]['avg_salary']) >= int(min_avg_salary) and int(filtered_rows[i]['saudi_stuff']) >= int(min_stuff):
                new_arr.append(filtered_rows[i])
                blured_arr.append(filtered_rows[i])
        except:
            print(filtered_rows[i]['avg_salary'], filtered_rows[i]['saudi_stuff'])
    return new_arr

def return_employee(application_id):
    filtered_rows = list(Employee.objects.all().values())
    new_arr = []

    for i in range(len(filtered_rows)):
        if str(filtered_rows[i]['id']) == application_id:
            new_arr.append(filtered_rows[i])

    return new_arr

def unlocked_applications(user):
    return bank_portal_new.objects.get(user_id=user.id).unlocked_applications.split()

def add_one(user, id):
    try:
        bank = bank_portal_new(user=user)
        bank.unlocked_applications = str(id)
        bank.count = 1
        bank.save()
    except:
        bank = bank_portal_new.objects.get(user_id=user.id)
        bank.unlocked_applications += f' {id}'
        bank.count += 1
    bank.save()