from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Exam

def home(request):
    return render(request, 'quiz/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'quiz/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentquiz')
            except IntegrityError:
                return render(request, 'quiz/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'quiz/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'quiz/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'quiz/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currentquiz')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def currentquiz(request):
    if request.method == 'GET':
        return render(request, 'quiz/currentquiz.html', {})
    else:
        return redirect('home')

@login_required
def attendquiz(request):
    quiz = Exam.objects.filter(examcompleted__isnull=True)
    if request.method == 'GET':
        return render(request, 'quiz/attendquiz.html', {'quiz':quiz})
    else:
        try:
            return redirect('currentquiz')
        except:
            return render(request, 'quiz/currentquiz.html', {'quiz':quiz, 'error':'Bad info'})
