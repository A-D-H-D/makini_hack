from django.core.mail import send_mail
from makini_hack.settings import EMAIL_HOST_USER
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POSTp['mesaage-email']
        message =request.POST['message']

        # send an email
        send_mail(
            message_name, #subjetc,
            message,
            message_email ,
            ['kariukibriankamotho@gmail.com'],
        )
    else:
        return render(request, 'contact.html', {})

    return render(request, 'contact.html', {})
