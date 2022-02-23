from django.db import models

# Create your models here.


class History(models.Model):
    u1 = models.CharField(max_length=50)
    u2 = models.CharField(max_length=50)
    u3 = models.CharField(max_length=50)
    k1 = models.CharField(max_length=50)
    k2 = models.CharField(max_length=50)
    k3 = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.u1
