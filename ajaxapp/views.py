from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    resp = 'Hello Ajax'
    return HttpResponse(resp, content_type='text/plain')

def getdata(request):
    
    name = request.data.get['newname']
    email = request.data.get['newemail']
    phone = request.data.get['newphone']
    print(name,email,phone)
    return HttpResponse(name, email, phone)