from django.shortcuts import render
from django.http import HttpResponse


def form(request):
    return render(request,'form.html')
def status(request):
    dh=dash.objects.all()
    return render(request,'status.html',{'dh':dh})
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
    