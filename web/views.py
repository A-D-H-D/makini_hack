from django.core.mail import send_mail
from makini_hack.settings import EMAIL_HOST_USER
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect,render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subjetc,
            message,
            message_email,
            ['kariukibriankamotho@gmail.com'],
        )
    else:
        return render(request, 'contact.html', {})

    return render(request, 'contact.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}')
            return redirect('index')
        else:
            messages.error(request, f'Invalid username or password')
            return redirect('login_user')
    # else:
    #     return render(request, 'login_user.html')
    return render(request, 'login_user.html', {})
