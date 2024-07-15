from django.db import models

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
