from django.db import models

class Pendiente(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=255)
    completed = models.BooleanField()

    def __str__(self):
        return self.title
