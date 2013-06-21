<<<<<<< HEAD
from django.shortcuts import render_to_response, get_object_or_404
from models import About, Page, Dynamic_Section, Announcement
from forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
=======
from django.shortcuts import render_to_response
from models import About, Page
>>>>>>> parent of 4819700... Updated Registration Form

    # This checks the subdomain, but is unnecessary, if only /blog is used
    # which means then the subdomain middleware can also be removed
    #
    # if request.subdomain == "blog":
    #   return render_to_response("blog.html")
    # else:


<<<<<<< HEAD
def home(request, page_number=1):
=======
def home(request):
>>>>>>> parent of 4819700... Updated Registration Form
    """
        Renders the home.html view which is used as the index page i.e
        url path is www.umonya.org/
    """
<<<<<<< HEAD
    page_number = int(page_number)
    announcements = Announcement.objects.order_by("-pub_date")
    total_announcements = len(announcements)

    # gets section of announcements wanted for page
    if total_announcements > 5:
        announcements = announcements[(page_number * 5)-5:page_number * 5]
        # get page numbers, and total pages
        if (total_announcements % 5):
            total_pages = (total_announcements // 5) + 1
        else:
            total_pages = (total_announcements // 5)
    else:
        announcements = announcements[:total_announcements]
        total_pages = 1
    prev = str(page_number - 1)
    next = str(page_number + 1)
    host = request.get_full_path()
    host_s = host.split('/')
    if len(host_s) > 2:
        if host_s[1] == "announcements":
            prev = "".join(["page", prev])
            next = "".join(["page", next])
            path = ""
    else:
        prev = "".join(["announcements/page", prev])
        next = "".join(["announcements/page", next])
        path = "announcements/"
    return render_to_response(
        "home.html",
        {'announcements': announcements,
        'page_number': page_number,
        'total_pages': total_pages,
        'prev': prev,
        'next': next,
        'path': path
        })


def view_announcement(request, page_number, slug):
    announcement = get_object_or_404(Announcement, slug=slug)
    return render_to_response("view_announcement.html", {
        'announcement': announcement,
        'page_number': page_number
        })
=======
    return render_to_response("home.html")

>>>>>>> parent of 4819700... Updated Registration Form


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
<<<<<<< HEAD
    # pub_date = Registration(pub_date=timezone.now())
    if request.method == "POST":
        # f = RegistrationForm(request.POST, instance=pub_date)
        f = RegistrationForm(request.POST)

        if f.is_valid():
            send_email_f(f)
            success = {"success": "success"}
            return render_to_response("registration.html", success,
                              context_instance=RequestContext(request))

    else:
        f = RegistrationForm()

    try:
        section = Dynamic_Section.objects.get(section="registration")
    except Dynamic_Section.DoesNotExist:
        section = False

    args = {}
    args.update(csrf(request))
    args["section"] = section
    args["form"] = f

    return render_to_response("registration.html", args,
                              context_instance=RequestContext(request))
=======
    """
        Renders the registration.html view which is used as the index
        page i.e url path is www.umonya.org/registration/
    """
    return render_to_response("registration.html")
>>>>>>> parent of 4819700... Updated Registration Form


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
<<<<<<< HEAD
    return render_to_response("blog.html", context_instance=RequestContext(request))


def send_email_f(f):
    from django.core.mail import send_mail
    subject = "User Registration"
    message = ''
    for item in f.cleaned_data:
        message = message + item.upper() + "\n" + str(f.cleaned_data[item]) + "\n\n"
    sender = "umonya@admin.com"
    recipients = ["umonya@admin.com"]
    send_mail(subject, message, sender, recipients)
=======
    """
        Renders the blog.html view which is used as the index page i.e
        url path is www.umonya.org/blog/
    """
    return render_to_response("blog.html")
>>>>>>> parent of 4819700... Updated Registration Form
