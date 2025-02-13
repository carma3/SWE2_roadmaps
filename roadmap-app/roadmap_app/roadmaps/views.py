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
            return redirect("dashboard")  # Redirect to a protected page
        else:
            messages.error(request, "Invalid username or password")

    # Else just render index.html
    return render(request, 'roadmaps/index.html')



def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save() # Save new AppUser in database with posted data
            login(request, user) # 
            messages.success(request, "Account created successfully!")
            return redirect('roadmaps/pages/dashboard.php')

    else:
        form = SignUpForm()

    

    # After setting "form" to SignUpForm, render the html page and
    # send it the form data under the alias 'form'
    return render(request, 'roadmaps/signup.html', {'form': form})

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

    if request.method == 'POST':
        try:
            data = json.loads(request.body) # Get the JSON from the request

            # Create roadmap with initial data
            roadmap = Roadmap.objects.create(
                roadmap_title=data.get("title"),
                roadmap_description=data.get("description")
            )

            student_ids = data.get("roadmap_students", []) # Get the student IDs from the JSON
            students = AppUser.objects.filter(id__in=student_ids)  # Retrieve students objects by IDs
            roadmap.roadmap_students.set(students)  # Associate students with the 
            
            roadmap.metadata.set(data)

            return JsonResponse(
                {"message": "Roadmap created successfully", "roadmap_id": roadmap.roadmap_id},
                status=201
            )
        
        except Exception as ex:
            return JsonResponse({"Error:" : str(ex)}, status=400)

    return JsonResponse({"Error" : "Invalid Request"}, status=405)