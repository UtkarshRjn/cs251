from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	followers = models.IntegerField(default=0)
	timing = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.user.username} Profile'

class Respository(models.Model):
	repo_name = models.CharField(max_length=120)
	stars = models.IntegerField()
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.repo_name}'