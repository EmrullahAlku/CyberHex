from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_accounts/profile.html', {'user': user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', user_id=user.id)
    else:
        form = UserCreationForm()
    return render(request, 'user_accounts/register.html', {'form': form})

def accounts_index(request):
    return render(request, 'user_accounts/accounts_index.html')
