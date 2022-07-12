from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    # will find user_list.html in templates folder
    return render(request, 'user_list.html')


def user_add(request):
    return render(request,'user_add.html')
