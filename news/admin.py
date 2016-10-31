from django.contrib import admin

from zinnia.admin import EntryAdmin
from zinnia.models.entry import Entry
from news.models import Photo
from news.models import EntryPhoto

class EntryPhotoInline(admin.TabularInline):
    model = EntryPhoto

class EntryAdmin(EntryAdmin):
    inlines = (EntryPhotoInline,)

admin.site.unregister(Entry)
admin.site.register(Photo)
admin.site.register(Entry, EntryAdmin)