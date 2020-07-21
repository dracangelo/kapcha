from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm, ReserveForm
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm 
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def send_mail(request):
    contact = Contact.objects.last()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']

            try:
                sm(subject, message, from_email, ['test@gmail.com'] )
            except BadHeaderError:
                return HttpResponse('invalid header')
            return redirect('contact:success')
    else:
        contact_form = ContactForm()

    
    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    
    else:
        reserve_form = ReserveForm()

    context = {
        'contact':contact,
        'contact_form':contact_form,
        'reserve_form': reserve_form
    }

    return render(request , 'contact/contact.html' , context)



def success(request):
    return HttpResponse('thanks you for you email ^_^')