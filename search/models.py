from django.db import models

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.TextField()
    lat_long = models.CharField(max_length=50)
    full_details = models.JSONField()

    def __str__(self):
        return self.name
