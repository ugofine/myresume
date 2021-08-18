from django.db import models

# Create your models here.

class Port(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank =True)
    url = models.URLField(max_length=250, blank=True)

   


    def __str__(self):
        return self.title
