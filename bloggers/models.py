from django.db import models

class Blogger(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    article_url = models.URLField()
    video_url = models.URLField()


    def __str__(self):
        return self.name
