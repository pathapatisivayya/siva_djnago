from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

from django.shortcuts import render


def dataview(request):    
    return render(request, 'index.html')

	 
	 
