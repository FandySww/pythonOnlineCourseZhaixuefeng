import os

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # 调用脚本
    req = request.GET.get('path')
    arg1 = request.GET.get('arg1')
    arg2 = request.GET.get('arg2')
    try:
        result = os.system(req + ' ' + arg1 + ' ' + arg2)
    except:
        return HttpResponse('调用出错')
    else:
        return HttpResponse('调用成功：'+str(result))
