from django.shortcuts import render_to_response, get_object_or_404
from models import About, Page, Dynamic_Section, Announcement
from forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

    # This checks the subdomain, but is unnecessary, if only /blog is used
    # which means then the subdomain middleware can also be removed
    #
    # if request.subdomain == "blog":
    #   return render_to_response("blog.html")
    # else:


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


def about(request):
    about = About.objects.all()
    page_content = Page.objects.all().filter(page="about")
    return render_to_response("about.html", {'about': about,
                              "page_content": page_content},
                              context_instance=RequestContext(request))


def resources(request):
    return render_to_response("resources.html", context_instance=RequestContext(request))


def registration(request):
    # pub_date = Registration(pub_date=timezone.now())
    if request.method == "POST":
        # f = RegistrationForm(request.POST, instance=pub_date)
        f = RegistrationForm(request.POST)

        if f.is_valid():
            send_email_f(f)
            return HttpResponseRedirect("/")

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
    return render_to_response("contact.html", context_instance=RequestContext(request))


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
    send_mail(subject, message, sender, recipients)
