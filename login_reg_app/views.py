from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def process_registration(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/')
    else:
        username = request.POST['username']
        email = request.POST['email']
        birthday = request.POST['birthday']
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(username=username, email=email, birthday=birthday, password=pw_hash)
        request.session['userid'] = user.id
        return redirect(f'/anisearch/')

def process_login(request):
    login_errors = User.objects.login_validator(request.POST)
    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value, extra_tags='login')
        return redirect('/')
    else:
        email = request.POST['email_login']
        password = request.POST['password_login']
        user = User.objects.filter(email=email)
        logged_user = user[0]
        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect(f'/anisearch/')