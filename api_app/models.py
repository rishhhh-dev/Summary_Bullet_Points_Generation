from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Text(models.Model):
    input_text = models.CharField(max_length=500)
    summary = models.TextField(null=True,default="")
    bullets =  ArrayField(models.CharField(max_length=500),null=True,default=[])

    def __str__(self):
        return super().__str__()

