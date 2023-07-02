from django.conf import settings
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    # To show category name in django
    def __str__(self):
        return self.title
    
    
class Course(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    
    def __str__(self):
        return self.title   
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'https://bulma.io/images/placeholders/1280x960.png'
        

