from django.shortcuts import render

# Create your views here.

def index(request):
    words = 'World!'
    return render(request, 'index.html', context={'words': words}) 
