from django.db import models
from .validators import file_size

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)


class Chart(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="Video/%y",validators=[file_size])
    def __str__(self):
        return self.caption

    