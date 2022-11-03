from django.contrib import admin

# Register your models here.
from .models import Articles


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
