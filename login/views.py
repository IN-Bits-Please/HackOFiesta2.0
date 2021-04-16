from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


def login(request):
    return render(request, 'base.html')


def signUp(request):
    return render(request, 'base.html')


def signUpInd(request):
    return render(request, 'base.html')


def signUpNgo(request):
    if request.method == "POST":
        first_name = request.POST['name']
        last_name = "NGO"
        email = request.POST['email']
        tagline = request.POST['tagline']
        password = request.POST['password']
        password_c = request.POST['password_repeat']
        if password == password_c:
            if User.objects.filter(email=email).exists():
                messages.info(request, "User already exists.")
                return redirect('/signUpNgo')
            user = User.objects.create_user(
                email=email, password=password, first_name=first_name, last_name=last_name, username=email)
            user.save()
            ngo_obj = Ngo(username=email, tagline=tagline)
            ngo_obj.save()
            messages.info(request, 'User created succesfully.')
            return redirect('/signUpNgo')

        else:
            messages.info(request, 'Passwords don\'t match')
            return redirect('/signUpNgo')
    return render(request, 'login/signUpNgo.html')
