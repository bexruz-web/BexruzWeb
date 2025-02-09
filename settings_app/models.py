from django.db import models


class TelegramBotSettings(models.Model):
    username = models.CharField(max_length=200)
    token = models.TextField()
    userid_list = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "TelegramBot Sozlamalari"
