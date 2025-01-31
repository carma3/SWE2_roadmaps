from django.shortcuts import render
from django.http import HttpResponse
from .models import Roadmap, Student

# Create your views here.

def home(request):
    return HttpResponse("Home Page!")

def roadmap_list(request):
    roadmaps = Roadmap.objects.all() # Gets all roadmaps from the db
    return render(request, 'roadmap_list.html', {"roadmaps" : roadmaps})
    # render syntax: 
    # render(HTTP request object, 
    # html file in templates directory, 
    # dictionary of data to pass to the template ({variable_name : roadmaps list}) )

