from django.shortcuts import render
from comics.forms import contact_form
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
#this is my contact page, or where the customer will be able to reach out to the store.
def contact(request):
    title = 'Contact'
    form = contact_form.contactForm(request.POST or None)
    confirm_message = None
#this if statement will print the request in the terminal if the request is valid
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True
        )
        title = "Thanks!"
        confirm_message = "Thank you for the message.  We'll get right back to you!"
        form = None

    context = {'title':title, 'form':form, 'confirm_message':confirm_message,}
    template = 'contact.html'
    return render(request, template, context)