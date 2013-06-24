from django.test import TestCase
from umonya.apps.main.models import About, Page, Dynamic_Section
import datetime
from django.utils.timezone import utc
from django.core.urlresolvers import reverse


class TestPages(TestCase):
    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_blog(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog.html")

    def test_about(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('about' in response.context)
        self.assertTrue('page_content' in response.context)
        self.assertTemplateUsed(response, "about.html")

    def test_registration(self):
        Dynamic_Section.objects.create(section="registration", enabled=True)
        response = self.client.get("/registration/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration.html")

    def test_resources(self):
        response = self.client.get("/resources/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "resources.html")

    def test_course(self):
        response = self.client.get("/course/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "course.html")

    def test_contact(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")


class TestPageContent(TestCase):
    def test_about_content(self):
        Page.objects.create(page="about",
                            content="<h1>Umonya heading</h1>")

        response = self.client.get("/about/")
        content = response.context['page_content'][0]
        self.assertEqual([a.pk for a in response.context['page_content']], [1])
        self.assertEqual(content.page, "about")
        self.assertEqual(content.content, "<h1>Umonya heading</h1>")

    def test_about_bios(self):
        About.objects.create(name="Umonya Name",
                             bios="Umonya Bios",
                             bios_photo="path/2/Um/Photo.png",
                             pub_date=datetime.datetime.utcnow().
                             replace(tzinfo=utc))

        response = self.client.get("/about/")
        content = response.context['about'][0]
        self.assertEqual([a.pk for a in response.context['about']], [1])
        self.assertEqual(content.name, "Umonya Name")
        self.assertEqual(content.bios, "Umonya Bios")
        self.assertEqual(content.bios_photo, "path/2/Um/Photo.png")

    def test_registration_open(self):
        Dynamic_Section.objects.create(section="registration", enabled=True)
        response = self.client.get("/registration/")
        self.assertTrue("section" in response.context)
        self.assertEqual(response.context["section"].enabled, True)
        self.assertContains(response, "</form>")
        self.assertNotContains(response, "registration has closed")

    def test_registration_closed(self):
        Dynamic_Section.objects.create(section="registration", enabled=False)
        response = self.client.get("/registration/")
        self.assertTrue("section" in response.context)
        self.assertEqual(response.context["section"].enabled, False)
        self.assertNotContains(response, "</form>")
        self.assertContains(response, "registration has closed")


class TestUrls(TestCase):
    def test_home_url(self):
        url = reverse("umonya.apps.main.views.home")
        self.assertEqual(url, "/")

    def test_about_url(self):
        url = reverse("umonya.apps.main.views.about")
        self.assertEqual(url, "/about/")

    def test_resources_url(self):
        url = reverse("umonya.apps.main.views.resources")
        self.assertEqual(url, "/resources/")

    def test_registration_url(self):
        url = reverse("umonya.apps.main.views.registration")
        self.assertEqual(url, "/registration/")

    def test_contact_url(self):
        url = reverse("umonya.apps.main.views.contact")
        self.assertEqual(url, "/contact/")

    def test_course_url(self):
        url = reverse("umonya.apps.main.views.course")
        self.assertEqual(url, "/course/")

    def test_blog_url(self):
        url = reverse("umonya.apps.main.views.blog")
        self.assertEqual(url, "/blog/")
