from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Ruby Carvalho',
    })


def contato(request):
    return render(request, 'recipes/contato.html')


def veja(request):
    return HttpResponse('veja')
