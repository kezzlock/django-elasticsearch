import requests
import json
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)
from .models import Articles
from .documents import NewsDocument
from .serializers import NewDocumentSerializer

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def generate_random_data():
    url = f"https://newsapi.org/v2/everything?q=Apple&from=2022-11-03&sortBy=popularity&apiKey={NEWS_API_KEY}"
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    for data in payload.get("articles"):
        print(count)
        Articles.objects.create(title=data.get("title"), content=data.get("content"))


def index(request):
    generate_random_data()
    return JsonResponse({"status": 200})


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = (
        "title",
        "content",
    )
    multi_match_search_fields = ("title", "content")
    filter_fields = {"title": "title", "content": "content"}
