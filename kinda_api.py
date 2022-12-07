from datetime import datetime, timedelta
# import pandas as pd

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