from django.db import models


# Create your models here.


class Person(models.Model):
    uuid = models.CharField(max_length=150, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.uuid


class Content(models.Model):
    content_slug = models.SlugField(max_length=100)
    drive_link = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.content_slug


class Downloads(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    content = models.ForeignKey(to=Content, on_delete=models.CASCADE)
    downloads = models.PositiveIntegerField(default=0)
