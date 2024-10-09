from django.urls import path
from .views import home, give_it_30

urlpatterns = [
    path('', home, name='home'),
    path('give_it_30/', give_it_30, name='give_it_30'),
]
