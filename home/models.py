from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    watch_count = models.IntegerField(default=0)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    tags = models.ManyToManyField(Tag)
    image = models.URLField(default=None, null=True)

    def __str__(self):
        return self.title
