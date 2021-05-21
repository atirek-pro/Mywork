from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import QuestionSerializer, AnswerSerializer
from questions.models import Question, Answer
from rest_framework import status, permissions


class QuestionAPIView(APIView):


    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        questions = Question.objects.filter(user=request.user.id)
        serializer = QuestionSerializer(questions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        data = {
            'user': request.user.id,
            'title': request.data.get('title'),
            'body': request.data.get('body')
        }

        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerAPIView(APIView):

    serializer_class = AnswerSerializer

    def get(self, request, *args, **kwargs):
        answers = Answer.objects.filter(user=request.user.id)
        serializer = AnswerSerializer(answers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = {
            'user': request.user.id,
            'parent': request.data.get('parent'),
            'body': request.data.get('body')
        }

        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


