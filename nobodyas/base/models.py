from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    image = models.ImageField(
        null=True, blank=True, upload_to="images", default='placeholder.jpg'
    )
    body = RichTextUploadingField()
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if Post.objects.filter(slug=self.slug).exists():
                self.slug = self.generate_unique_slug(self.slug)
        super().save(*args, **kwargs)

    def generate_unique_slug(self, slug):
        base_slug = slugify(self.title)
        count = 1
        new_slug = base_slug
        while Post.objects.filter(slug=new_slug).exists():
            new_slug = f"{base_slug}-{count}"
            count += 1
        return new_slug

    def __str__(self) -> str:
        return self.title


class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    image = models.ImageField(
        null=True, blank=True, upload_to="images", default='placeholder.jpg'
    )
    tags = models.ManyToManyField(Tag, null=True)
    link = models.URLField()

    def __str__(self) -> str:
        return self.title
