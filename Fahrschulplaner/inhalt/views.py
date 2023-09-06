

from django.shortcuts import render, redirect
from .forms import contact_form
from django.http import HttpResponse
from django.core.mail import EmailMessage
# Create your views here.

# returns index Homepage
def index(request):
    return render(request, 'index.html')

# returns success after sending email
def success(request):
    return HttpResponse(request, 'Success!')

# Email setup for Contact_form
def contact(request):
        # checking if POST is True
        if request.method == 'POST':
            form = contact_form(request.POST)
            # checking if form is_valid
            if form.is_valid():
                # claiming Data
                email = form.cleaned_data['EMail_Adresse']
                message = form.cleaned_data['Beschreibung']
                
                # submitting Email
                EmailMessage(
                    'Contact Form Submission from {}'.format(email), message,
                    email,['k3nkox@gmail.com'],
                    [],[],
                    reply_to=[email]
                ).send()
                
                return redirect('success')
        # if false, return contact.html
        else:
            form = contact_form()
            return render(request, 'contact.html', {'form': form})
        
        