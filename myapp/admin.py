from django.contrib import admin
from django.contrib.admin import register
# Register your models here.
from myapp.models import EpisodeDetail, ShowDetail, ShowsImagesDocuments, \
    EpisodesImagesDocuments, EpisodesAudiosDocuments


@register(ShowsImagesDocuments)
class ShowsImagesDocumentsAdmin(admin.ModelAdmin):
    list_display = ["doc_id", "doc_file_path"]


@register(EpisodesImagesDocuments)
class EpisodesImagesDocumentsAdmin(admin.ModelAdmin):
    list_display = ["doc_id", "doc_file_path"]


@register(EpisodesAudiosDocuments)
class EpisodesAudiosDocumentsAdmin(admin.ModelAdmin):
    list_display = ["doc_id", "doc_file_path"]


@register(ShowDetail)
class ShowDetailAdmin(admin.ModelAdmin):
    list_display = ["show_uuid", "title", "description"]


@register(EpisodeDetail)
class EpisodeDetailAdmin(admin.ModelAdmin):
    list_display = ["episode_uuid", "title", "description"]

