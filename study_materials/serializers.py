from rest_framework.serializers import ModelSerializer
from study_materials.models import FlashCard, FlashCardItem, Quiz, QuizQuestion, QuizQuestionOption, Matching, MatchingItem, Note

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