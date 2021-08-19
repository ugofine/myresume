from django.shortcuts import render
from .models import Contact, Port
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    portfolio = Port.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

    return render(request, 'pages/index.html', {'portfolio' : portfolio})

