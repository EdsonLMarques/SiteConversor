from django.urls import path
from . import views

urlpatterns = [
     path('characters', views.characters, name='characters'),
     path('enconding', views.enconding, name='enconding'),
     path('chartoNumbers', views.chartoNumbers, name='chartoNumbers'),
]
