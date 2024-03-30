from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def virat(request):
    return render(request,"virat.html")

def abd(request):
    return HttpResponse('abd is the best finisher of the ipl death overs')