from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter
from .models import Post, Author



class PostFilter(FilterSet):
       class Meta:
        model = Post
        fields = {
        'dateCreation': ['gt'],
        # 'title': ['icontains'],
         'author':['exact'],
        }
