from django.db import models
from django.contrib.auth.models import User

class ProductMC(models.Model):
    title = models.CharField(max_length= 250)
    url = models. URLField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to = 'Images/')
    icon = models.ImageField(upload_to = 'Images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    def pub_date_nice(self):
        return self.pub_date.strftime('%b %e %Y')
    def summary(self):
        return self.body[:100]
    #hunter
