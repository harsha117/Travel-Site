from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'name' : 'Harsha'})


def addmul(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    addres = val1 + val2
    mulres = val1 * val2

    return render(request, 'result.html', {'addresult' : addres, 'mulresult' : mulres})


# def mul(request):
#
#     value1 = int(request.GET['numm1'])
#     value2 = int(request.GET['numm2'])
#
#     ress = value1 * value2
#     return render(request, 'result.html', {'mulresult': ress})

# Create your views here.


