from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')

def user_list(request):
    return HttpResponse('用户列表')

def user_add(request):
    return HttpResponse('添加用户')