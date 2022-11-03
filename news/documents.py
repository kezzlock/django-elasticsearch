from django_elasticsearch_dsl import Document, fields, Index

from .models import Articles

# articles = Index("articles")

PUBLISHER_INDEX = Index("elastic_demo")
PUBLISHER_INDEX.settings(number_of_shards=1, number_of_replicas=1)


@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    id = fields.IntegerField(attr="id")
    title = fields.TextField(attr="title")
    content = fields.TextField(fields={"raw": {"type": "keyword"}})

    class Django(object):
        model = Articles
