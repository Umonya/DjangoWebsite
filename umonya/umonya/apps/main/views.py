from django.shortcuts import render_to_response
from models import About

	# This checks the subdomain, but is unnecessary, if only /blog is used
	# which means then the subdomain middleware can also be removed
	#
	# if request.subdomain == "blog":
	#	return render_to_response("blog.html")
	# else:

def home(request):
	return render_to_response("home.html")
	
def about(request):
	about			= About.objects.all()
	
	return render_to_response("about.html", {'about': about})
	
def resources(request):
	return render_to_response("resources.html")
	
def registration(request):
	return render_to_response("registration.html")
	
def contact(request):
	return render_to_response("contact.html")
	
def course(request):
	return render_to_response("course.html")

def blog(request):
	return render_to_response("blog.html")
	
