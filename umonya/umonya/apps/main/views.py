from django.shortcuts import render_to_response
from models import About, Page, Dynamic_Section, Registration
from forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.template import RequestContext

    # This checks the subdomain, but is unnecessary, if only /blog is used
    # which means then the subdomain middleware can also be removed
    #
    # if request.subdomain == "blog":
    #   return render_to_response("blog.html")
    # else:


def home(request):
    return render_to_response("home.html", context_instance=RequestContext(request))


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
