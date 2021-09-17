from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile, Respository
from .forms import SignUpForm 
import requests

# Create your views here.
def home(request):
	context = {
		'profiles': Profile.objects.all()
	}
	return render(request, 'home.html', context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('username')
			fetch(name)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'loginapi/signup.html', {'form': form})

def explore(request):
	context = {
		'profiles': Profile.objects.all()
	}
	return render(request, 'explore.html',context)

def fetch(name):
	
	user = User.objects.filter(username = name).first()
	# profile fetch
	response = requests.get('https://api.github.com/users/{}'.format(user.username))
	data = response.json()
	profile = Profile(followers=data['followers'],user_id=user.id)
	profile.save()
	# repo fetch
	response = requests.get('https://api.github.com/users/{}/repos'.format(user.username))
	respositories = response.json()
	for repo_dict in respositories:
		repo = Respository(repo_name = repo_dict['name'],stars= repo_dict['stargazers_count'], profile_id = profile.id)
		repo.save()

@login_required
def profile(request, user_id):
	user = User.objects.get(id=user_id)
	repos = Respository.objects.filter(profile_id = user.id)
	return render(request, 'profile.html', {'this_user': user, 'repos': repos})
