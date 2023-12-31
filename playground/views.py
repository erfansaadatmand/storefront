from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return render(request,'hello.html', {'name':'paul'})

def say_hello_all(request):
    return render(request, 'hell.html')    