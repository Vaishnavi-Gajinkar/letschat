from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    # form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Successfully created for '+ user)
            return redirect('chat/index')
    else:
        form = CreateUserForm()
    return render(request,'accounts/register.html', {'form':form})

def home(request):
    return render(request,'accounts/dashboard.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'accounts/login.html', context)
    context ={}
    return render(request,'accounts/login.html', context)

def customers(request):
    return render(request,'accounts/customers.html')

def products(request):
    return render(request,'accounts/products.html')