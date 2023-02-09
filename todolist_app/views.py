from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    context = {
        'Welcome_text':"welcome to todolist page.",
    }
    return render(request, 'todolist.html', context)

def contact(request):
    context = {
        'Contact_text':"welcome to contact page.",
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'About_text':"welcome to about page.",
    }
    return render(request, 'about.html', context)
