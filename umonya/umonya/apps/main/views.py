from django.shortcuts import render_to_response

def home(request):
	return render_to_response("home.html")
	
def about(request):
	return render_to_response("about.html")
	
def resources(request):
	return render_to_response("resources.html")
	
def registration(request):
	return render_to_response("registration.html")
	
def contact(request):
	return render_to_response("contact.html")
	
def course(request):
	return render_to_response("course.html")
	
	
