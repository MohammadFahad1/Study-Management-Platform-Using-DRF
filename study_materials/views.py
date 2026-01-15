from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from study_materials.models import FlashCard, FlashCardItem, Quiz, QuizQuestion, Matching, MatchingItem, Note
from user.models import User, OTP
from study_materials.serializers import FlashCardSerializer, FlashCardItemSerializer, QuizSerializer, QuizQuestionSerializer, MatchingSerializer, MatchingItemSerializer, NoteSerializer, ForgotPasswordSerializer
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from study_materials.filters import FlashCardFilter, QuizFilter
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
import random
import datetime
from rest_framework.permissions import AllowAny

class ForgotPasswordView(GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serilaizer = self.serializer_class(data=request.data)
        serilaizer.is_valid(raise_exception=True)

        email = serilaizer.validated_data['email']
        user = get_object_or_404(User, email=email)
        otp = str(random.randint(100000, 999999))
        print(otp)
        payload = {
            'user': user,
            'code': otp,
            'expires_at': datetime.datetime.now() + datetime.timedelta(minutes=5),
            'is_used': False,
        }

        OTP.objects.create(**payload)

        send_mail(
            'OTP for Password Reset - Study Management Platform',
            f'Your OTP for password reset is: {otp}. This OTP is valid for 5 minutes.',
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        return Response({
            'message': 'OTP has been sent to your email address.'
        }, status=200)
    
class VerifyOTPView(GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)    
        email = serializer.validated_data.get('email')
        otp = serializer.validated_data.get('otp')
        user = get_object_or_404(User, email=email)
        otp_obj = OTP.objects.filter(user=user, code=otp, is_used=False).first()
        if otp_obj:
            otp_obj.is_used = True
            otp_obj.save()
            return Response({
                'message': 'OTP verified successfully.'
            }, status=200)
        else:
            return Response({
                'message': 'Invalid OTP.'
            }, status=400)



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