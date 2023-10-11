from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to="images", default='placeholder.jpg'
    )
    body = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag, null=True)

    def get_absolute_url(self):
        return reverse("post", kwargs={"id": self.pk})

    def __str__(self) -> str:
        return self.title
