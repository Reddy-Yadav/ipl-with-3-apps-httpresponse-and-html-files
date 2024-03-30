from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('raina is a first order batesman')