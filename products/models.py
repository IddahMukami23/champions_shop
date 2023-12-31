from PIL import Image
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    qtty = models.CharField(max_length=100, blank=False, null=False)
    price = models.CharField(max_length=100, blank=False, null=False)
    desc = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to='static/images/products/')

    # The def function below overrides the image saving
    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height < 462 or img.width < 340:
            output_size = (462, 340)
            img.thumbnail(output_size)
            img.save(self.image.path)


def __str__(self):
    return self.name
