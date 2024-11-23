from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
 
class Image(models.Model):
    """ Image model to database, this is to store all images available for users to pick from,
    images will be stored in Cloudinary"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image_url = CloudinaryField('image', default='https://res.cloudinary.com/your_cloud_name/image/upload/vdefault_placeholder.jpg')

    def __str__(self):
        return self.title
