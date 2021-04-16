from django.shortcuts import render


def login(request):
    return render(request, 'base.html')


def signUp(request):
    return render(request, 'base.html')


def signUpInd(request):
    return render(request, 'base.html')


def signUpNgo(request):
    return render(request, 'base.html')
