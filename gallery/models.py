from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='gallery_imgs/')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.title, self.created_date)
