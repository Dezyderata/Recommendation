from django.shortcuts import render, redirect
from recommendationApp import forms
# Create your views here.


def index(request):
    return render(request, 'recommendationApp/index.html')


def form_user_view(request):
    form = forms.UserForm()
    success_url = '/'
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #return redirect(success_url)
            return index(request)
        else:
            print('ERROR, form invalid!')
    return render(request, 'recommendationApp/form_page.html', {'form': form})


