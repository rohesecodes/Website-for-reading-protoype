from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'] )
            if user is not None:
                login(request, user)
                return render(request, 'users/index.html')
            else:
                return HttpResponse("invalid credentials")


    else:
        form = LoginForm()
    return render(request,'users/login.html',{'form': form})

@login_required
def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_done.html')

    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})

def catalogue(request):
    return render(request, 'users/showAllBooks.html')

