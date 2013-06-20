from django.contrib import admin
from models import Announcement, About, Page, Registration, Dynamic_Section

#~ Ensuring that admin is aware of this class
admin.site.register(Announcement)
admin.site.register(About)
admin.site.register(Page)
admin.site.register(Registration)
admin.site.register(Dynamic_Section)
