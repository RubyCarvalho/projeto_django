from django.urls import path

from recipes.views import contato, home, veja

urlpatterns = [
    path('', home),
    path('contato', contato),
    path('veja', veja),
]
