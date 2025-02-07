from django.contrib import admin

from about_me.models import About, ContactMessages


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'name', 'age', 'address', 'email', 'phone', 'resume_link']
admin.site.register(About, AboutAdmin)


class ContactMessagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'text']
admin.site.register(ContactMessages, ContactMessagesAdmin)