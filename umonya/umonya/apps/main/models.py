from django.db import models
from time import time

def get_image_path(instance, filename):
	return "img/pic/bios/%s_%s" % (str(time()).replace(".",'_'), filename)
	
class Announcement(models.Model):
	title		= models.CharField(max_length = 200)
	body		= models.TextField()
	pub_date	= models.DateTimeField("date published")
	event_date	= models.DateTimeField("Event Date")
	location	= models.CharField(max_length = 300)

class About(models.Model):
	name		= models.CharField(max_length = 200)
	role		= models.CharField(max_length = 200)
	bios		= models.TextField()
	bios_photo	= models.ImageField(upload_to = get_image_path, blank = True, null = True)
	pub_date	= models.DateTimeField("date published")
