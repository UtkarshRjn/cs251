from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
import requests

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	followers = models.IntegerField()
	timing = models.DateTimeField(auto_now=False, auto_now_add=False)

	# @receiver(post_save, sender=User)
	# def create_user_profile(sender, instance, created, **kwargs):
	#     if created:
	#         Profile.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def save_user_profile(sender, instance, **kwargs):
	#     instance.profile.save()

	# def update_profile(request, user_id):
	#     user = User.objects.get(pk=user_id)
	#     response = requests.get('https://api.github.com/users/{}'.format(user.username))
	#     data = response.json()
	#     user.profile.followers = data['followers']
	#     user.profile.timing = datetime.now()
	#     user.save()

class Respository(models.Model):
	repo_name = models.CharField(max_length=120)
	stars = models.IntegerField()
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
