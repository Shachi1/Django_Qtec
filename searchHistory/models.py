from django.db import models

# Create your models here.


class History(models.Model):
    user = models.CharField(max_length=50)
    search = models.CharField(max_length=50)

    def __str__(self):
        return self.search
