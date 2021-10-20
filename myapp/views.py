import datetime
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from media import settings
from myapp.models import ShowDetail, EpisodeDetail, EpisodesAudiosDocuments, EpisodesImagesDocuments, \
    ShowsImagesDocuments
from myapp.serializers import ShowDetailSerializer, EpisodeDetailSerializer


""" Show detail's CRUD """


class ShowDetailListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            show = ShowDetail.objects.filter(is_deleted=False)
            serializer = ShowDetailSerializer(show, many=True)
            return Response(serializer.data)

        except:
            return Response(
                data={"message": "Shows List Not Found."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class ShowDetailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            id = self.kwargs["show_uuid"]
            show = ShowDetail.objects.get(show_uuid=id)
            serializer = ShowDetailSerializer(show)
            return Response(serializer.data)

        except:
            return Response(
                data={"message": "Show Detail not found", "isEmpty": "true"},
            )


class ShowDetailCreateView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        show_data = data
        serializer = ShowDetailSerializer(data=show_data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save(validated_data=show_data)
        fellowship = ShowDetail.objects.get(show_uuid=result)
        serializer = ShowDetailSerializer(fellowship)
        return Response(serializer.data)


class ShowDetailDeleteView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):

        id = self.kwargs["show_uuid"]
        religion = ShowDetail.objects.get(show_uuid=id)
        try:

            religion.is_deleted = True
            religion.save()
            return Response(
                data={"message": "Record Deleted Successfully."},
            )
        except:
            return Response(
                data={"message": "Details Not Found."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class ShowDetailUpdateView(APIView):
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        id = self.kwargs["show_uuid"]
        data = self.request.data
        show_data = data
        show = ShowDetail.objects.get(show_uuid=id)
        serializer = ShowDetailSerializer(
            show, data=show_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=show, validated_data=show_data)
        serializer = ShowDetailSerializer(show)
        return Response(serializer.data)


""" Episode detail's CRUD """
class EpisodeDetailListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):

        try:
            show = EpisodeDetail.objects.filter(is_deleted=False)
            serializer = EpisodeDetailSerializer(show, many=True)
            return Response(serializer.data)

        except:
            return Response(
                data={"message": "Episodes List Not Found."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class EpisodeDetailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):

        try:
            id = self.kwargs["episode_uuid"]
            show = EpisodeDetail.objects.get(episode_uuid=id)
            serializer = EpisodeDetailSerializer(show)
            return Response(serializer.data)

        except:
            return Response(
                data={"message": "Episode Detail not found", "isEmpty": "true"},
            )


class EpisodeDetailCreateView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        episode_data = data
        serializer = EpisodeDetailSerializer(data=episode_data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save(validated_data=episode_data)
        fellowship = EpisodeDetail.objects.get(episode_uuid=result)
        serializer = EpisodeDetailSerializer(fellowship)
        return Response(serializer.data)


class EpisodeDetailDeleteView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):

        id = self.kwargs["episode_uuid"]
        religion = EpisodeDetail.objects.get(episode_uuid=id)
        try:

            religion.is_deleted = True
            religion.save()
            return Response(
                data={"message": "Record Deleted Successfully."},
            )
        except:
            return Response(
                data={"message": "Details Not Found."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class EpisodeDetailUpdateView(APIView):
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        id = self.kwargs["episode_uuid"]
        data = self.request.data
        show_data = data
        show = EpisodeDetail.objects.get(episode_uuid=id)
        serializer = EpisodeDetailSerializer(
            show, data=show_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=show, validated_data=show_data)
        serializer = EpisodeDetailSerializer(show)
        return Response(serializer.data)


"""  Files Upload API on Cloud server """


class FileUpload(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if "file" not in request.data:
            return Response(
                data={"messege": "No file Found"},
            )

        file = request.data["file"]
        doc_name = ""
        doc_type = self.request.GET["doc_type"]
        filename, extension = os.path.splitext(file.name)
        timestamp = int(datetime.datetime.now().timestamp())
        filename = f"{filename}_{timestamp}{extension}"
        if doc_type == "show_image":
            allowed_extensions = [".jpg", ".jpeg", ".png"]
            if extension.lower() in allowed_extensions:
                path = f"shows_image_documents/show/show_image/{filename}"
                default_storage.save(
                    f"{settings.MEDIA_ROOT}/{path}",
                    ContentFile(file.read()),
                )
                temp_path = f"{settings.BASE_URL}{settings.MEDIA_URL}{path}"
                doc = ShowsImagesDocuments.objects.create(doc_file_path=temp_path)

            else:
                return Response(
                    data={"messege": "Enter file of type jpg,jpeg and png."},
                )
        elif doc_type == "episode_image":
            allowed_extensions = [".jpg", ".jpeg", ".png"]
            if extension.lower() in allowed_extensions:
                path = f"episodes_image_documents/episode/episode_image/{filename}"
                default_storage.save(
                    f"{settings.MEDIA_ROOT}/{path}",
                    ContentFile(file.read()),
                )
                temp_path = f"{settings.BASE_URL}{settings.MEDIA_URL}{path}"
                doc = EpisodesImagesDocuments.objects.create(doc_file_path=temp_path)

            else:
                return Response(
                    data={"messege": "Enter file of type jpg,jpeg and png."},
                )

        elif doc_type == "episode_audio":
            path = f"episodes_audio_documents/episode/episode_audio/{filename}"
            default_storage.save(
                f"{settings.MEDIA_ROOT}/{path}",
                ContentFile(file.read()),
            )
            default_storage.save(
                f"{settings.MEDIA_ROOT}/{path}", ContentFile(file.read())
            )
            temp_path = f"{settings.BASE_URL}{settings.MEDIA_URL}{path}"
            if doc_type == "episode_audio":
                doc = EpisodesAudiosDocuments.objects.create(doc_file_path=temp_path)

        else:
            path = f"applicant_documents/others/{filename}"
            default_storage.save(
                f"{settings.MEDIA_ROOT}/{path}", ContentFile(file.read())
            )
        return Response(
            data={
                "messege": "File uploaded successfully",
                "doc_file_path": doc.doc_file_path,
                "doc_name": doc_name or filename,
                "doc_id": doc.doc_id,
            }
        )

