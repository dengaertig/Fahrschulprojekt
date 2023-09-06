

from django.shortcuts import render, redirect
from .forms import contact_form
from django.http import HttpResponse
from django.core.mail import EmailMessage
# Create your views here.

def index(request):
    return render(request, 'index.html')

def success(request):
    return HttpResponse(request, 'Success!')

def contact(request):
        if request.method == 'POST':
            form = contact_form(request.POST)
            if form.is_valid():
                name = form.cleaned_data['Vorname']
                email = form.cleaned_data['EMail_Adresse']
                message = form.cleaned_data['Beschreibung']
                
                EmailMessage(
                    'Contact Form Submission from {}'.format(email), message,
                    email,['k3nkox@gmail.com'],
                    [],[],
                    reply_to=[email]
                ).send()
                
                return redirect('success')
        else:
            form = contact_form()
            return render(request, 'contact.html', {'form': form})
        
        