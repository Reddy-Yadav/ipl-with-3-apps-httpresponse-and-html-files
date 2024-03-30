from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')

def bumhra(request):
    return HttpResponse('boom boom bumhra')
