from rest_framework.serializers import ModelSerializer
from study_materials.models import FlashCard, FlashCardItem, Quiz, QuizQuestion, Matching, MatchingItem, Note

class FlashCardItemSerializer(ModelSerializer):
    class Meta:
        model = FlashCardItem
        fields = ['id', 'question', 'answer']
class FlashCardSerializer(ModelSerializer):
    items = FlashCardItemSerializer(many=True, read_only=True)
    class Meta:
        model = FlashCard
        fields = ['id', 'user', 'title', 'items', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

class QuizQuestionSerializer(ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'question', 'answer', 'rationale', 'option_a', 'option_b', 'option_c', 'option_d']

class QuizSerializer(ModelSerializer):
    questions = QuizQuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['id', 'user', 'title', 'questions', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

class MatchingItemSerializer(ModelSerializer):
    class Meta:
        model = MatchingItem
        fields = ['id', 'term', 'definition']

class MatchingSerializer(ModelSerializer):
    items = MatchingItemSerializer(many=True, read_only=True)
    class Meta:
        model = Matching
        fields = ['id', 'user', 'title', 'items', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'user', 'title', 'subtitle', 'note', 'notesubtitle', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']