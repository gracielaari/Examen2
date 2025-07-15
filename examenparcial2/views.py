from django.shortcuts import render

def index(request):
    return render(request, 'examenparcial2/index.html')
