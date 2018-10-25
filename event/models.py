from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    ticket_price = models.IntegerField()
    place=models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    organizing_company= models.CharField(max_length=500)
    company_address = models.CharField(max_length=500)
    image = models.ImageField(upload_to='profile_images/')
    fb_link = models.CharField(max_length=500,blank=True)
    twiter_link = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return '%s %s' % (self.title, self.starting_date)




