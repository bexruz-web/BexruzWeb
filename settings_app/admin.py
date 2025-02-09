from django.contrib import admin

from settings_app.models import TelegramBotSettings


class TelegramBotSettingsAdmin(admin.ModelAdmin):
    list_display = ['username', 'token']
admin.site.register(TelegramBotSettings, TelegramBotSettingsAdmin)