from django_filters.rest_framework import FilterSet
from study_materials.models import FlashCard

class FlashCardFilter(FilterSet):
    class Meta:
        model = FlashCard
        fields = {
            'title': ['icontains'],
            'created_at': ['gte', 'lte'],
            'updated_at': ['gte', 'lte'],
        }