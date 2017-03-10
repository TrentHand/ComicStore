from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.

#this is my home page, or where the customer will land initially
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

#this is my about page, or where the customer will learn about the company
def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)

#this is the user profile page, and it can only be accessed when the user is logged in
@login_required 
def userProfile(request):
    user = request.user
    context = {'user':user}
    template = 'profile.html'
    return render(request, template, context)