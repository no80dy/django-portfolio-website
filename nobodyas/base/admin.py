from django.contrib import admin

from .models import Post, Tag, PortfolioProject


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(PortfolioProject)
class ProtfolioProjectAdmin(admin.ModelAdmin):
    pass
