from django.conf.urls import url
from django.urls import path, include
from .views import (
    QuestionAPIView, AnswerAPIView
)

urlpatterns = [
    path('', QuestionAPIView.as_view()),
    path('answer/', AnswerAPIView.as_view()),
]