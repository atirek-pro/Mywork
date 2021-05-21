from rest_framework import serializers
from questions.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    class Meta:
        model = Question
        fields = [
            'user',
            'title',
            'body',
            'created_at',
            'updated_at'
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'user',
            'question',
            'parent',
            'body',
            'created_at',
            'updated_at'
        ]





