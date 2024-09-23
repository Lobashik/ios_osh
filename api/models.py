from django.db import models

# иконка, название, вес, описание, еще что-то

class Icons(models.Model):
    picture = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.CharField(max_length=20)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100)
