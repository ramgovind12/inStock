from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')

            if not any(messages.get_messages(request)):
                user = User.objects.create(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.set_password(password)
                user.save()
                return redirect('credentials:login')
        else:
            messages.info(request,'Verify Password')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('shop:allProdCat')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('shop:allProdCat')