from django.db import models

# Create your models here.

class Topics(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.TextField()
    large_description = models.TextField()

    def __str__(self) :
        return self.name


