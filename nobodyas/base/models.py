from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self) -> str:
        return self.title
