from django.db import models
from django.utils import timezone
from time import time


def get_image_path(instance, filename):
    """
        Returns the file path to store the images which is passed to the
        database
    """
    return "img/pic/bios/%s_%s" % (str(time()).replace(".", '_'), filename)


class Announcement(models.Model):
    '''
    Model for announcements
    Stores title, body, event date, venue (can be blank)
    Date Published set on save.
    '''
    title = models.CharField(
        max_length=200,
        unique=True
        )

    body = models.TextField()

    pub_date = models.DateField(
        "Date Published",
        default=timezone.now().date(),
        editable=False
        )
    event_date = models.DateTimeField(
        "Event Date",
        default=timezone.now())
    venue = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ["pub_date"]

    def __unicode__(self):
        return u"%s %s" % (self.title, self.pub_date)

    def save(self):
        '''
        Custom save function sets Date Published to current time on save
        '''
        self.slug = self.title.replace(" ","_")
        self.pub_date = timezone.now().date()
        super(Announcement, self).save()

    def is_valid_date(self):
        """ Checks if event date has passed """
        if (self.event_date.date() < self.pub_date):
            return False
        return True


class About(models.Model):
    """
        The About Model stores the umonya team personal data i.e. the
        content to be displayed in the \about page
    """
    name = models.CharField(max_length=200)
    bios = models.TextField()
    bios_photo = models.ImageField(upload_to=get_image_path,
                                   blank=True, null=True)
    pub_date = models.DateTimeField("Date Published")

    def __unicode__(self):
        return self.name


class Page(models.Model):
    """
        The Page Model is used to populate content in each of the
        individual pages, the content is stored as HTML in the database
    """
    page = models.CharField(max_length=200)
    content = models.TextField()

    def __unicode__(self):
        return self.page


class Registration(models.Model):
    """
        Model that generates specific sections in the User Form
    """
    TYPE_OF_Q = (("CharField", "CharField"), ("EmailField", "EmailField"),
                 ("IntegerField", "IntegerField"), ("TextField", "TextField"))

    name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=200, choices=TYPE_OF_Q)
    text = models.CharField(max_length=200)
    priority = models.IntegerField()
    required = models.BooleanField()

    def __unicode__(self):
        return self.name


class Dynamic_Section(models.Model):
    """
        Sections that can be enabled or disabled by admin such as registration form and menu
    """
    section = models.CharField(max_length=200)
    enabled = models.BooleanField()

    def __unicode__(self):
        return self.section


class Contact(models.Model):
    pass
