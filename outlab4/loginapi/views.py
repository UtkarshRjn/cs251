from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Profile, Respository
from .forms import SignUpForm 
import requests
from datetime import datetime

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
			user = User.objects.filter(username = name).first()
			profile_data, respositories = fetch(user)
			save(user, profile_data, respositories)
			return redirect('/accounts/login')
	else:
		form = SignUpForm()
	return render(request, 'loginapi/signup.html', {'form': form})

def explore(request):
	context = {
		'profiles': Profile.objects.all()
	}
	return render(request, 'explore.html',context)

def fetch(user):
	
	# profile fetch
	response = requests.get('https://api.github.com/users/{}'.format(user.username))
	profile_data = response.json()
	# repo fetch
	response = requests.get('https://api.github.com/users/{}/repos'.format(user.username))
	respositories = response.json()

	return profile_data, respositories

def save(user, profile_data, respositories):
	# save profile
	profile = Profile(followers=profile_data['followers'],user_id=user.id)
	profile.save()
	# save repositories
	for repo_dict in respositories:
		repo = Respository(repo_name = repo_dict['name'],stars= repo_dict['stargazers_count'], profile_id = profile.id)
		repo.save()

@login_required
def profile(request, user_id):
	user = User.objects.get(id=user_id)
	repos = Respository.objects.filter(profile_id = user.profile.id).order_by('-stars')
	return render(request, 'profile.html', {'this_user': user, 'repos': repos})

def profile_update(request, user_id):
	user = User.objects.get(id=user_id)
	profile_data, respositories = fetch(user)
	update(user, profile_data, respositories)
	return redirect('/profile/{}'.format(user_id)) 

def update(user, profile_data, respositories):

	profile = Profile.objects.filter(user_id= user.id)
	profile.update(followers=profile_data['followers'], timing= datetime.now())

	for repo_dict in respositories:
		repo = Respository.objects.filter(repo_name= repo_dict['name'])
		if(repo.exists()):
			repo.update(stars= repo_dict['stargazers_count'])
		else:
			new_repo = Respository(repo_name = repo_dict['name'],stars= repo_dict['stargazers_count'], profile_id = profile.id)
			new_repo.save()