from django.db import models


class About(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    resume_link = models.FileField(upload_to='resume')

    class Meta:
        verbose_name_plural = "About sahifasi"

    def __str__(self):
        return self.name


class ContactMessages(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return self.name




