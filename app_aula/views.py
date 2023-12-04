from django.shortcuts import render

def home (requests):
    return render(requests, "app_aula/home.html")

def desenvolvedor1 (requests):
    return render(requests, "app_aula/desenvolvedor1.html")

def desenvolvedor2 (requests):
    return render(requests, "app_aula/desenvolvedor2.html")

def desenvolvedor3 (requests):
    return render(requests, "app_aula/desenvolvedor3.html")