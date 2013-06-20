from django.shortcuts import render_to_response
from models import About, Page

    # This checks the subdomain, but is unnecessary, if only /blog is used
    # which means then the subdomain middleware can also be removed
    #
    # if request.subdomain == "blog":
    #   return render_to_response("blog.html")
    # else:


def home(request):
    """
        Renders the home.html view which is used as the index page i.e
        url path is www.umonya.org/
    """
    return render_to_response("home.html")


def about(request):
    """
        Renders the about.html view which is used as the index page i.e
        url path is www.umonya.org/about/.
        The view populates the content from data stored in the database
    """
    about = About.objects.all()
    page_content = Page.objects.all().filter(page="about")
    return render_to_response("about.html", {'about': about,
                              "page_content": page_content})


def resources(request):
    """
        Renders the resources.html view which is used as the index
        page i.e url path is www.umonya.org/resources
    """
    return render_to_response("resources.html")


def registration(request):
    """
        Renders the registration.html view which is used as the index
        page i.e url path is www.umonya.org/registration/
    """
    return render_to_response("registration.html")


def contact(request):
    """
        Renders the contact.html view which is used as the index page
        i.e url path is www.umonya.org/contact/
    """
    return render_to_response("contact.html")


def course(request):
    """
        Renders the course.html view which is used as the index page i.e
        url path is www.umonya.org/course/
    """
    return render_to_response("course.html")


def blog(request):
    """
        Renders the blog.html view which is used as the index page i.e
        url path is www.umonya.org/blog/
    """
    return render_to_response("blog.html")
