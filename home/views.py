from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validations(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    User.objects.register(request.POST)
    new_user = User.objects.get(username=request.POST['username'])
    request.session['user_id'] = new_user.id
    return redirect('/dashboard')

def login(request):
    result = User.objects.authenticate(request.POST['username'], request.POST['password'])
    if result == False:
        messages.error(request,"Invalid Username/Password")
    else:
        user = User.objects.get(username = request.POST['username'])
        request.session['user_id'] = user.id
        return redirect('/dashboard')
    return redirect('/')

def dashboard(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')