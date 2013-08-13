from django.contrib import admin
from notes.models import Note
from notes.models import Category

class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'text', 'cat', 'user']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'

admin.site.register(Note, NoteAdmin)
admin.site.register(Category)