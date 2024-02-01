from django.db import models

from .consts import MAX_RATE

RATE_CHOICES = {(x,str(x)) for x in range(0, MAX_RATE + 1)}

class Creation(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    video = models.FileField(upload_to="videos/")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Review(models.Model):
    creation = models.ForeignKey(Creation, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



