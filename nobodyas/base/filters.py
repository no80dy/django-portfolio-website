from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter
from django.forms import CheckboxSelectMultiple

from .models import Post, Tag


class PostFilter(FilterSet):
    title = CharFilter(
        field_name='title', lookup_expr='icontains', label='Title'
    )
    tags = ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ['title', 'tags', ]
