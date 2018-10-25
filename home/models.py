from django.db import models

# Create your models here.
class HomeBanner(models.Model):
    heading =models.CharField(max_length=500)
    created_date =models.DateTimeField(auto_now=True)
    content= models.TextField()
    background_image = models.ImageField(upload_to='background_imgs/', blank=True)

    def __str__(self):
        return '%s %s' % (self.heading, self.content)
