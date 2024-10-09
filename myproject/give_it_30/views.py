from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GiveIt30

def home(request):
    count = None
    if request.user.is_authenticated:
        give_it_30, created = GiveIt30.objects.get_or_create(user=request.user)
        count = give_it_30.count
    return render(request, 'give_it_30/home.html', {'count': count})

@login_required
def give_it_30(request):
    give_it_30, created = GiveIt30.objects.get_or_create(user=request.user)
    give_it_30.count += 1
    give_it_30.save()
    return redirect('home')