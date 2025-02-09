from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    filter = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=250)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='portfolios')
    link = models.CharField(max_length=400)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Portfoliolar"