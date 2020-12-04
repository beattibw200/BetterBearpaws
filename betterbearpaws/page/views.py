from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'name': 'Ethan'});

def combine(request):
    newName = request.POST["name"]
    studentName = newName +" 's"
    studentuser = request.POST["username"]
    studentpass = request.POST["password"]
    return render(request, 'home.html', {"studentName": studentName});
