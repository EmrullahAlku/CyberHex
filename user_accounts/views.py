from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout

@login_required  
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {'user': user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', user_id=user.id)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def accounts_index(request):
    return render(request, 'accounts_index.html')

def custom_logout(request, user_id):
    
    logout(request)
    return redirect('/')

def custom_login(request, user_id):
    
    login(request)
    return redirect('/')
