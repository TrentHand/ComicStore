from django.shortcuts import render

# Create your views here.

#this is my home page, or where the customer will land initially
def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

#this is my about page, or where the customer will learn about the company
def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)