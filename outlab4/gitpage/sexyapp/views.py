from django.urls import reverse_lazy
from django.views import generic
from django import forms
from requests.api import request
from .models import Profile
from django.shortcuts import redirect, render,HttpResponse
from .forms import SignUpForm

def register(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sexyapp')
    else:
        form = SignUpForm()

        args = {'form': form}
        return render(request, 'registration/signup.html',args)
