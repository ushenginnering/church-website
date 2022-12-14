from django.contrib import admin
from .models import LeadPastors, BookLibrary, VideoMessage, NewsLetter, NewsLetterUsers, PrayerRequest, AdminTutorial

class VideoMessageAdmin(admin.ModelAdmin):
    fields = ('url',)

# Register your models here.
admin.site.register(LeadPastors)
admin.site.register(BookLibrary)
admin.site.register(VideoMessage, VideoMessageAdmin)
admin.site.register(NewsLetter)
admin.site.register(NewsLetterUsers)
admin.site.register(PrayerRequest)
admin.site.register(AdminTutorial)


from django.contrib.sites.models import Site
from cms.models import Page, PageType, StaticPlaceholder

admin.site.unregister(Site)
admin.site.unregister(Page)
admin.site.unregister(PageType)
admin.site.unregister(StaticPlaceholder)