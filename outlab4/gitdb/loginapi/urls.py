from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
	path('explore/', views.explore, name='explore'),
	path('profile/<user_id>/', views.profile),
]