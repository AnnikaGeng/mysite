#_*_ coding: utf-8 _*_

from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")