from django.shortcuts import render, redirect
from recommendationApp import forms
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'recommendationApp/index.html')


def login_page(request):
    return render(request, 'recommendationApp/login_page.html')


def main(request):
    return render(request, 'recommendationApp/main.html')


def register_user(request):
    form = forms.UserForm()
    #success_url = '/'
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #return redirect(success_url)
            return redirect('/main/')
        else:
            print('ERROR, form invalid!')
    return render(request, 'recommendationApp/registration_page.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/main/')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")
    form = forms.LoginForm(request.POST)
    return render(request, 'recommendationApp/login_page.html', context={"login_form": form})
