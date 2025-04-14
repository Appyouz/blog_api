from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name="articles")

    def __str__(self) -> str:
        return self.title
