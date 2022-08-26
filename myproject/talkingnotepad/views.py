from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    '''
    return HttpResponse("Hello, World. You're at the polls index.")
    '''
    template = loader.get_template('talkingnotepad/index.html')
    return render(request, 'talkingnotepad/index.html')
    