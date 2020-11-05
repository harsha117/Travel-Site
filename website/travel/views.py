from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Destination


def hyderabad(request):

    if request.user.is_authenticated:
        return render(request, 'destinations/hyderabad.html')

    else:
        messages.info(request, "Please login to check this page")
        return redirect('accounts/login')


# for dest_name in dest_names:
#     if dest_name == "Hyderabad":
#         def hyderabad(request):
#             if request.user.is_authenticated:
#                 return render(request, 'destinations/hyderabad.html')
#
#             else:
#                 return redirect('accounts/login')


def mumbai(request):
    if request.user.is_authenticated:
        return render(request, 'destinations/mumbai.html')

    else:
        messages.info(request, "Please login to check this page")
        return redirect('accounts/login')


def chennai(request):
    if request.user.is_authenticated:
        return render(request, 'destinations/chennai.html')

    else:
        messages.info(request, "Please login to check this page")
        return redirect('accounts/login')


def banglore(request):
    if request.user.is_authenticated:
        return render(request, 'destinations/banglore.html')

    else:
        messages.info(request, "Please login to check this page")
        return redirect('accounts/login')


def pune(request):
    if request.user.is_authenticated:
        return render(request, 'destinations/pune.html')

    else:
        messages.info(request, "Please login to check this page")
        return redirect('accounts/login')

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests' : dests})

# Create your views here.
