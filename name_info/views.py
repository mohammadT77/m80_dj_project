from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def get_info_view(request):
    if request.method == 'GET':
        return render(request, 'name_info/index.html')
    elif request.method == 'POST':
        
        return HttpResponse(request.POST['name'])
    else:
        return HttpResponse("Invalid method", status=405)
