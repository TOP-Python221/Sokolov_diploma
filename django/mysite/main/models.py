from django.db import models


class SpongeCake(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.TextField()

    @property
    def __str__(self):
        return self.name
