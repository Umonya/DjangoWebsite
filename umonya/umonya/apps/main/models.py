from django.db import models
from time import time


def get_image_path(instance, filename):
    """
        Returns the file path to store the images which is passed to the
        database
    """
    return "img/pic/bios/%s_%s" % (str(time()).replace(".", '_'), filename)


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField("date published")
    event_date = models.DateTimeField("Event Date")
    location = models.CharField(max_length=300)


class About(models.Model):
    """
        The About Model stores the umonya team personal data i.e. the
        content to be displayed in the \about page
    """
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bios = models.TextField()
    bios_photo = models.ImageField(upload_to=get_image_path,
                                   blank=True, null=True)
    pub_date = models.DateTimeField("date published")


class Page(models.Model):
    """
        The Page Model is used to populate content in each of the
        individual pages, the content is stored as HTML in the database
    """
    page = models.CharField(max_length=200)
    content = models.TextField()
