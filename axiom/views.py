from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def project_index(request):
    return render(request, 'index.html')

def link_a(request):
    return render(request, 'process.html')

def link_b(request):
    return render(request, 'bc.html')

def link_c(request):
    return render(request, 'flow.html')

def link_d(request):
    return render(request, 'stages.html')

def link_e(request):
    return render(request, 'stats.html')