from django.shortcuts import render, redirect
from django.db import connection
import hashlib

# HASH PASSWORD
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

from django.shortcuts import render

def home(request):
    if not request.session.get('user_id'):
        return redirect('login')
    return render(request, 'base.html')

# REGISTER
def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = hash_password(request.POST['password'])

        with connection.cursor() as cursor:
            cursor.callproc('RegisterUser', [name, email, password])

        return redirect('login')

    return render(request, 'auth/register.html')


# LOGIN
def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = hash_password(request.POST['password'])

        with connection.cursor() as cursor:
            cursor.callproc('LoginUser', [email])
            user = cursor.fetchone()

        if user and user[3] == password:
            request.session['user_id'] = user[0]
            request.session['user_name'] = user[1]
            return redirect('home')

    return render(request, 'auth/login.html')
    

def logout_view(request):
    request.session.flush()
    return redirect('login')    