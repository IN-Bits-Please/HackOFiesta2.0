from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('signUp', views.signUp),
    path('signUpInd', views.signUpInd),
    path('signUpNgo', views.signUpNgo)
]
