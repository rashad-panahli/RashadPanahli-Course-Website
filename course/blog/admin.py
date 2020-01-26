from django.contrib import admin
from .models import Post, Contact

class ContactAdmin (admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'create_at')
    list_filter = ('status', 'create_at')


admin.site.register( Contact, ContactAdmin)
admin.site.register(Post)