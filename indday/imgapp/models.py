from django.db import models

class ImgApp(models.Model):
    image = models.URLField(max_length=1000,editable=False)
    card_title = models.CharField(max_length=50)
    card_description = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.card_title
