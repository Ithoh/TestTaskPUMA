from django.shortcuts import render
from .models import Employee
import json
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def index(request):
    employee_list = list(Employee.objects.all().values())
    context = {'employee_list_json': json.dumps(employee_list, default=json_serial)}

    return render(request, 'EmployeeTable/index.html', context)