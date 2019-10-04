from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='pic_folder/')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()

    def __str__(self):
        return self.image_name


class Location(models.Model):
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
