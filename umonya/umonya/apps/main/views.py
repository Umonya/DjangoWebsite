from django.shortcuts import render_to_response, get_object_or_404
from models import About, Page, Dynamic_Section, Announcement
from forms import RegistrationForm, ContactForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

def home(request, page_number=1):
    """
        Renders the home.html view which is used as the index page i.e
        url path is www.umonya.org/
    """
    page_number = int(page_number)
    announcements = Announcement.objects.order_by("-pub_date")
    total_announcements = len(announcements)

    # gets section of announcements wanted for page
    if total_announcements > 5:
        announcements = announcements[(page_number * 5)-5:page_number * 5]
        # get page numbers, and total pages
        total_pages = total_announcements // 5
        total_pages += total_announcements % 5 and 1 or 0
    else:
        announcements = announcements[:total_announcements]
        total_pages = 1
    prev = str(page_number - 1)
    next = str(page_number + 1)
    host = request.get_full_path()
    host_s = host.split('/')
    if len(host_s) > 2:
        if host_s[1] == "announcements":
            prev = "page%s" % (prev)
            next = "page%s" % (next)
            path = ""
    else:
        prev = "anouncements/page%s" % (prev)
        next = "anouncements/page%s" % (next)
        path = "announcements/"
    return render_to_response(
        "home.html",
        {'announcements': announcements,
        'page_number': page_number,
        'total_pages': total_pages,
        'prev': prev,
        'next': next,
        'path': path,
        }, context_instance=RequestContext(request))


def view_announcement(request, page_number, slug):
    """
        Renders the view_announcement.html view which is used 
        to show announcements 
        i.e. url path is www.umonya.org/announcements/<page_number><slug> .
        The announcement is found by the slug stored in the database
    """
    announcement = get_object_or_404(Announcement,slug=slug)
    return render_to_response("view_announcement.html", {
        'announcement': announcement,
        'page_number': page_number
        })


def custom_404(request, page_number, slug):
    """
        Renders the custom_404.html view which is used 
        if the page is not found
        i.e. url path is www.umonya.org/something .
    """
    return render_to_response("custom_404.html",)


def about(request):
    about = About.objects.all()
    page_content = Page.objects.all().filter(page="about")
    return render_to_response("about.html", {'about': about,
                              "page_content": page_content},
                              context_instance=RequestContext(request))


def resources(request):
    return render_to_response("resources.html", context_instance=RequestContext(request))


def registration(request):
    if request.method == "POST":
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


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_email_f(form)
            success = {"success": "success"}
            return render_to_response("contact.html", success,
                                      context_instance=RequestContext(request))
    else:
        form = ContactForm
    args = {}
    args.update(csrf(request))
    args["form"] = form
    return render_to_response("contact.html", args,
                              context_instance=RequestContext(request))


def course(request):
    return render_to_response("course.html", context_instance=RequestContext(request))


def blog(request):
    return render_to_response("blog.html", context_instance=RequestContext(request))


def send_email_f(f):
    from django.core.mail import send_mail
    subject = "User Registration"
    message = ''
    for item in f.cleaned_data:
        message = message + item.upper() + "\n" + str(f.cleaned_data[item]) + "\n\n"
    sender = "umonya@admin.com"
    recipients = ["umonya@admin.com"]
    if send_mail(subject, message, sender, recipients):
        return True
