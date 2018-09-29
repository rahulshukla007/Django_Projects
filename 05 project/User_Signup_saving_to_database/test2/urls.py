from django.urls import path

#from test2 import views as user_views  #we can also write that

from . import views

urlpatterns = [
    path('regist/', views.register, name='registration'),
]