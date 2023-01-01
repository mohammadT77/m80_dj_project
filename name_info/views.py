from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from name_info.utils import *


def get_info_view(request):
    if request.method == 'GET':
        return render(request, 'name_info/index.html')
    elif request.method == 'POST':
        name = request.POST['name']
        return render(request, 'name_info/info.html', {
            'name': name,
            'gender': get_gender(name),
            'nationalities': get_nationalities(name),
            'age': get_age(name)
        })
    else:
        return HttpResponse("Invalid method", status=405)
