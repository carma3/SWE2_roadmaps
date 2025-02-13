from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Roadmap, AppUser
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def home(request):
    return HttpResponse("Home Page!")

# Get the username and password from index.html POST and authenticate against User table
def login_view(request):
    # When index.html posts to itself, authenticate and redirect if successful
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect("dashboard")  # Redirect to a protected page
        else:
            messages.error(request, "Invalid username or password")

    # Else just render index.html
    return render(request, 'roadmaps/index.html')



def signup_view(request):
    # If we post, populate the form with the post data, make sure it is valid, then save the new user,
    # log in, and redirect to their dashboard
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save() # Save new AppUser in database with posted data
            login(request, user) # Login and redirect to dashboard (save session data in request)
            request.session['username'] = request.POST['username']
            messages.success(request, "Account created successfully!")
            return redirect('roadmaps/pages/dashboard.php')

    else:
        form = SignUpForm()

    

    # After setting "form" to SignUpForm, render the html page and
    # send it the form data under the alias 'form'
    return render(request, 'roadmaps/signup.html', {'form': form})


def logout_view(request):
    logout(request)

    return redirect('login')

def dashboard(request):
    return render(request, 'roadmaps/pages/dashboard.php')

# List roadmaps page
def roadmap_list(request):
    roadmaps = Roadmap.objects.all() # Gets all roadmaps from the db
    return render(request, 'roadmaps/roadmap_list.html', {"roadmaps" : roadmaps})
    # render syntax: 
    # render(HTTP request object, 
    # html file in templates directory, 
    # dictionary of data to pass to the template {variable_name : roadmaps list} )

# Create roadmap page
def create_roadmap_form(request):
    return render(request, 'roadmaps/create-roadmap-form.html')

# Create roadmap post request
def create_roadmap(request):
    """
    Takes JSON data from front end and creates the object in the DB
    """
    pass