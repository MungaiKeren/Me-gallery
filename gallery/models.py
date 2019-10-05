from django.db import models


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update_location()

    @classmethod
    def get_location(cls):
        place = Location.objects.all()
        return place

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update_category()

    @classmethod
    def get_all_categories(cls):
        all_categories = Category.objects.all()
        return all_categories

    def __str__(self):
        return self.category


class Image(models.Model):
    """
    image class model that gets our image
    """
    image = models.ImageField(upload_to='pic_folder/')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    img_location = models.ForeignKey(Location)
    img_category = models.ForeignKey(Category)

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

    # @classmethod
    # def get_by_location(cls, location_id):
    #     image_location = Image.objects.filter_by(location__id=location_id)
    #     return image_location
    #
    # @classmethod
    # def get_by_category(cls, category_id):
    #     image_category = Image.objects.filter_by(category__id=category_id)
    #     return image_category

    class Meta:
        ordering = ['image']

    def __str__(self):
        return self.image_name


