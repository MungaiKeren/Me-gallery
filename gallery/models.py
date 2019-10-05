from django.db import models


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Image(models.Model):
    """
    image class model that gets our image
    """
    image = models.ImageField(upload_to='pic_folder/')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

    def __str__(self):
        return self.image_name
