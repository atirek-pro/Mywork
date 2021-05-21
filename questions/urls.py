from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('question/', include('questions.api.urls')),
]