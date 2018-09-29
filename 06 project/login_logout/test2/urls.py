from django.urls import path
from django.contrib.auth import views as auth_views

#from test2 import views as user_views  #we can also write that

from . import views

urlpatterns = [
    path('regist/', views.register, name='registration'),
    path('login/',auth_views.LoginView.as_view(template_name = 'test2/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='test2/logout.html'),name='logout'),
    path('profile/',views.profile, name='profile')
]
