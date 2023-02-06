from django.db import models


class Group(models.Model):
    class Meta:
        app_label = 'readingGroup'
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
