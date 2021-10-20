from rest_framework import serializers

from myapp.models import ShowDetail, ShowsImagesDocuments, EpisodesImagesDocuments, EpisodesAudiosDocuments, \
    EpisodeDetail


class ShowsImagesDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowsImagesDocuments
        fields = (
            "doc_id",
            "doc_file_path",
        )


class EpisodesImagesDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodesImagesDocuments
        fields = (
            "doc_id",
            "doc_file_path",
        )


class EpisodesAudiosDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodesAudiosDocuments
        fields = (
            "doc_id",
            "doc_file_path",
        )


class ShowDetailSerializer(serializers.ModelSerializer):
    image = ShowsImagesDocumentsSerializer(many=True, read_only=True)

    class Meta:
        model = ShowDetail
        fields = (
            "show_uuid",
            "title",
            "description",
            "image",
        )

    def save(self, validated_data):

        show_detail = ShowDetail.objects.create(
            title=validated_data["title"]
            if "title" in validated_data
            else None,

            description=validated_data["description"]
            if "description" in validated_data
            else None)

        for zonal_data in validated_data["image"]:
            single_image = ShowsImagesDocuments.objects.get(doc_id=zonal_data['doc_id'])
            show_detail.image.add(single_image)
        else:
            None

        show_detail.save()
        return show_detail.show_uuid

    def update(self, instance, validated_data):

        instance.title = (
            validated_data["title"]
            if validated_data["title"]
            else instance.title
        )

        instance.description = (
            validated_data["description"]
            if validated_data["description"]
            else instance.description
        )

        instance.image.clear()
        images = [img['doc_id'] for img in validated_data["image"]]
        instance.image.add(*images)

        instance.save()


class EpisodeDetailSerializer(serializers.ModelSerializer):
    image = EpisodesImagesDocumentsSerializer(many=True, read_only=True)
    audio = EpisodesAudiosDocumentsSerializer(many=True, read_only=True)

    class Meta:
        model = EpisodeDetail
        fields = (
            "episode_uuid",
            "title",
            "description",
            "image",
            "audio",
        )

    def save(self, validated_data):

        episode = EpisodeDetail.objects.create(
            title=validated_data["title"]
            if "title" in validated_data
            else None,

            description=validated_data["description"]
            if "description" in validated_data
            else None)

        for img_data in validated_data["image"]:
            single_image = EpisodesImagesDocuments.objects.get(doc_id=img_data['doc_id'])
            episode.image.add(single_image)
        else:
            None
        for audio_data in validated_data["audio"]:
            single_audio = EpisodesAudiosDocuments.objects.get(doc_id=audio_data['doc_id'])
            episode.audio.add(single_audio)
        else:
            None

        episode.save()
        return episode.episode_uuid

    def update(self, instance, validated_data):

        instance.title = (
            validated_data["title"]
            if validated_data["title"]
            else instance.title
        )

        instance.description = (
            validated_data["description"]
            if validated_data["description"]
            else instance.description
        )
        instance.image.clear()
        images = [img['doc_id'] for img in validated_data["image"]]
        instance.image.add(*images)

        instance.audio.clear()
        audios = [aud['doc_id'] for aud in validated_data["audio"]]
        instance.audio.add(*audios)
        instance.save()
