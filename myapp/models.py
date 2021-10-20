import uuid

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_by = models.CharField(
        max_length=50, null=True, blank=True, help_text="username"
    )
    updated_by = models.CharField(
        max_length=25, null=True, blank=True, help_text="username"
    )
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False, help_text="Used for Soft Delete")

    class Meta:
        abstract = True


class ShowsImagesDocuments(BaseModel):
    doc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    doc_file_path = models.CharField(
        max_length=500, null=True, blank=True, help_text="path to document"
    )

    def __str__(self):
        return str(self.doc_id)


class EpisodesImagesDocuments(BaseModel):

    doc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doc_file_path = models.CharField(
        max_length=500, null=True, blank=True, help_text="path to document"
    )

    def __str__(self):
        return str(self.doc_id)


class EpisodesAudiosDocuments(BaseModel):

    doc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doc_file_path = models.CharField(
        max_length=500, null=True, blank=True, help_text="path to document"
    )

    def __str__(self):
        return str(self.doc_id)


class ShowDetail(BaseModel):
    show_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title  = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ManyToManyField(
        "myapp.ShowsImagesDocuments", blank=True, null=True, related_name="show_images"
    )

    def __str__(self):
        return self.title


class EpisodeDetail(BaseModel):
    episode_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ManyToManyField(
        "myapp.EpisodesImagesDocuments", blank=True, null=True, related_name="episode_image"
    )
    audio = models.ManyToManyField(
        "myapp.EpisodesAudiosDocuments", blank=True, null=True, related_name="episode_audio"
    )

    def __str__(self):
        return self.title





