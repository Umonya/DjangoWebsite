from django.contrib import admin
from models import Announcement, About, Page

#~ Ensuring that admin is aware of this class

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title","pub_date","event_date","venue")
    search_fields = ("title", "body", "venue")
    list_filter = ("pub_date",)
    odering = ("pub_date")
    fields = ("title", "body", "event_date","venue")

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(About)
admin.site.register(Page)
