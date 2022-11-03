from .models import Articles
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import NewsDocument


class NewDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Articles
        document = NewsDocument

        fields = (
            "title",
            "content",
        )

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
