from django.http import HttpResponse
from django.template import loader
from HiPage.models import Good, Size
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic

def IndexView(request):
    return render(request, 'HiPage/homepage.html')

def Men(request):
    context = {'SIZE': Good.objects.all()}
    return render(request, 'HiPage/men.html', context)

def AboutUs(request):
    return render(request, 'HiPage/AboutUs.html')

def Terms(request):
    return render(request, 'HiPage/Terms.html')

def Delivery(request):
    return render(request, 'HiPage/Delivery.html')

def Refund(request):
    return render(request, 'HiPage/Refund.html')

def Support(request):
    return render(request, 'HiPage/Support.html')
