from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from study_materials.models import FlashCard, FlashCardItem, Quiz, QuizQuestion, Matching, MatchingItem, Note
from study_materials.serializers import FlashCardSerializer, FlashCardItemSerializer, QuizSerializer, QuizQuestionSerializer
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from study_materials.filters import FlashCardFilter

class FlashCardViewSet(ModelViewSet):
    serializer_class = FlashCardSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FlashCardFilter
    search_fields = ['question', 'answer']
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        return FlashCard.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FlashCardItemViewSet(ModelViewSet):
    serializer_class = FlashCardItemSerializer

    def get_queryset(self):
        if 'flashcard_pk' in self.kwargs:
            flashcard = FlashCard.objects.get(pk=self.kwargs['flashcard_pk'])
            if flashcard.user != self.request.user:
                raise PermissionDenied("You do not have permission to view items for this flashcard.")
        return FlashCardItem.objects.filter(flash_card=self.kwargs['flashcard_pk'])
    
    def perform_create(self, serializer):
        if self.request.user != FlashCard.objects.get(pk=self.kwargs['flashcard_pk']).user:
            raise PermissionDenied("You do not have permission to add items to this flashcard.")
        serializer.save(flash_card_id=self.kwargs['flashcard_pk'])


class QuizViewSet(ModelViewSet):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)