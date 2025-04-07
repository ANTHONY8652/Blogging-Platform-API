import django_filters
from .models import Blog_Post

class BlogPostFilter(django_filters.FilterSet):
    published_date = django_filters.DateFilter(field_name="published_date", lookup_expr='exact')
    category = django_filters.CharFilter(field_name="category", lookup_expr='iexact')

    class Meta:
        model = BlogPost
        fields = ['published_date', 'category']
