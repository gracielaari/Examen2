import requests
from django.shortcuts import render

# Create your views here.

API_URL = 'https://jsonplaceholder.typicode.com/todos'

def index(request):
    return render(request, 'pendientes/index.html')

def solo_ids(request):
    pendientes = requests.get(API_URL).json()
    solo_ids = [p['id'] for p in pendientes]
    return render(request, 'pendientes/solo_ids.html', {'pendientes': solo_ids})

def ids_titles(request):
    pendientes = requests.get(API_URL).json()
    return render(request, 'pendientes/ids_titles.html', {'pendientes': pendientes})

def no_resueltos(request):
    pendientes = requests.get(API_URL).json()
    filtrados = [p for p in pendientes if not p['completed']]
    return render(request, 'pendientes/no_resueltos.html', {'pendientes': filtrados})

def resueltos(request):
    pendientes = requests.get(API_URL).json()
    filtrados = [p for p in pendientes if p['completed']]
    return render(request, 'pendientes/resueltos.html', {'pendientes': filtrados})

def ids_user(request):
    pendientes = requests.get(API_URL).json()
    datos = [{'id': p['id'], 'userId': p['userId']} for p in pendientes]
    return render(request, 'pendientes/ids_user.html', {'pendientes': datos})

def resueltos_user(request):
    pendientes = requests.get(API_URL).json()
    datos = [{'id': p['id'], 'userId': p['userId']} for p in pendientes if p['completed']]
    return render(request, 'pendientes/resueltos_user.html', {'pendientes': datos})

def no_resueltos_user(request):
    pendientes = requests.get(API_URL).json()
    datos = [{'id': p['id'], 'userId': p['userId']} for p in pendientes if not p['completed']]
    return render(request, 'pendientes/no_resueltos_user.html', {'pendientes': datos})

