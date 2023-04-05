from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.core.mail import send_mail
from project1 import settings
from .forms import ContactForm


# Create your views here.
def hello(request):
    return HttpRequest('welcome django')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            recipients = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, email, recipients)
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def index(request):

  return render(request, 'index.html')

def blog(request):
    return render(request,'blog.html')



    