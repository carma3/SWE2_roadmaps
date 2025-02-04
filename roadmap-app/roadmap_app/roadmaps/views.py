from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Roadmap, Student
import json

# Test


# Create your views here.

def home(request):
    return HttpResponse("Home Page!")


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
            students = Student.objects.filter(id__in=student_ids)  # Retrieve students objects by IDs
            roadmap.roadmap_students.set(students)  # Associate students with the 
            
            roadmap.metadata.set(data)

            return JsonResponse(
                {"message": "Roadmap created successfully", "roadmap_id": roadmap.roadmap_id},
                status=201
            )
        
        except Exception as ex:
            return JsonResponse({"Error:" : str(ex)}, status=400)

    return JsonResponse({"Error" : "Invalid Request"}, status=405)