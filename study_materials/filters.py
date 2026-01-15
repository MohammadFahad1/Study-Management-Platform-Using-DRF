from django_filters.rest_framework import FilterSet
from study_materials.models import FlashCard, Quiz

class FlashCardFilter(FilterSet):
    class Meta:
        model = FlashCard
        fields = {
            'title': ['icontains'],
            'created_at': ['gte', 'lte'],
            'updated_at': ['gte', 'lte'],
        }

class QuizFilter(FilterSet):
    class Meta:
        model = Quiz
        fields = {
            'title': ['icontains'],
            'created_at': ['gte', 'lte'],
            'updated_at': ['gte', 'lte'],
        }