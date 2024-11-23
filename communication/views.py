from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# testing app set up with http response
def communication(request):
    return HttpResponse("Communication App is running!")
