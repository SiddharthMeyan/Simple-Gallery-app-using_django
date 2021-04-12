from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name
    

class Photos(models.Model):
    image = models.ImageField(null=False, blank=False)
    category = models.ForeignKey(Categories,on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=500)

    def __str__(self):
        self.user_desc=self.desc[:40]
        return self.user_desc+ ' ...'
    