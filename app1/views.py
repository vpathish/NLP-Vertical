from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "app1/index.html")

def faculty_training(request):
    return render(request,"app1/faculty_training.html")

def patents(request):
    return render(request,"app1/patents.html")

def publications(request):
    return render(request,"app1/publications.html")

def invited_talks(request):
    return render(request,"app1/invited_talks.html")

def inhouse_project(request):
    return render(request,"app1/inhouse_project.html")
    
def consultancy_projects(request):
    return render(request,"app1/consultancy_projects.html")