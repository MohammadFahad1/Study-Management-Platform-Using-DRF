from django.urls import path, include
from rest_framework_nested import routers
from study_materials.views import FlashCardViewSet, FlashCardItemViewSet, QuizViewSet, QuizQuestionViewSet

router = routers.DefaultRouter()
router.register('flashcards', FlashCardViewSet, basename='flashcards')
router.register('quizzes', QuizViewSet, basename='quizzes')

flashcard_router = routers.NestedDefaultRouter(router, 'flashcards', lookup='flashcard')
flashcard_router.register('items', FlashCardItemViewSet, basename='flashcard-items')

quizzes_router = routers.NestedDefaultRouter(router, 'quizzes', lookup='quiz')
quizzes_router.register('questions', QuizQuestionViewSet, basename='quiz-questions')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(flashcard_router.urls)),
    path('', include(quizzes_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]