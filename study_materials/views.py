from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from study_materials.models import FlashCard, FlashCardItem, Quiz, QuizQuestion, Matching, MatchingItem, Note
from study_materials.serializers import FlashCardSerializer, FlashCardItemSerializer, QuizSerializer, QuizQuestionSerializer, MatchingSerializer, MatchingItemSerializer, NoteSerializer
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from study_materials.filters import FlashCardFilter, QuizFilter

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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = QuizFilter
    search_fields = ['title']
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class QuizQuestionViewSet(ModelViewSet):
    serializer_class = QuizQuestionSerializer

    def get_queryset(self):
        if 'quiz_pk' in self.kwargs:
            quiz = Quiz.objects.get(pk=self.kwargs['quiz_pk'])
            if quiz.user != self.request.user:
                raise PermissionDenied("You do not have permission to view questions for this quiz.")
        return QuizQuestion.objects.filter(quiz=self.kwargs['quiz_pk'])
    
    def perform_create(self, serializer):
        if self.request.user != Quiz.objects.get(pk=self.kwargs['quiz_pk']).user:
            raise PermissionDenied("You do not have permission to add questions to this quiz.")
        serializer.save(quiz_id=self.kwargs['quiz_pk'])


class MatchingViewSet(ModelViewSet):
    serializer_class = MatchingSerializer

    def get_queryset(self):
        return Matching.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MatchingItemViewSet(ModelViewSet):
    serializer_class = MatchingItemSerializer

    def get_queryset(self):
        if 'matching_pk' in self.kwargs:
            matching = Matching.objects.get(pk=self.kwargs['matching_pk'])
            if matching.user != self.request.user:
                raise PermissionDenied("You do not have permission to view items for this matching.")
        return MatchingItem.objects.filter(matching=self.kwargs['matching_pk'])
    
    def perform_create(self, serializer):
        if self.request.user != Matching.objects.get(pk=self.kwargs['matching_pk']).user:
            raise PermissionDenied("You do not have permission to add items to this matching.")
        serializer.save(matching_id=self.kwargs['matching_pk'])

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)