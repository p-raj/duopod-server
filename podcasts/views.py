from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from podcasts.models import Subscription, Episode, Language, ListenStats, EpisodeLanguageMapping
from podcasts.serializers import SubscriptionSerializer, EpisodeSerializer, LanguagesSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    """

    """
    model = Subscription
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.action == 'retrieve':
                return SubscriptionSerializer
            else:
                return SubscriptionSerializer
        else:
            return SubscriptionSerializer

    def get_form_object(self, pk):
        return get_object_or_404(Subscription, pk=pk)

    def get_queryset(self):
        """
        """
        qs = self.model.objects.order_by("-id")
        return qs


class UserSubscriptionViewSet(viewsets.ModelViewSet):
    """

    """
    model = Subscription
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.action == 'retrieve':
                return SubscriptionSerializer
            else:
                return SubscriptionSerializer
        else:
            return SubscriptionSerializer

    def get_form_object(self, pk):
        return get_object_or_404(Subscription, pk=pk)

    def get_queryset(self):
        """
        """
        user = self.kwargs.get('userId')
        qs = self.model.objects.filter(subscriber=user).order_by("-id")
        return qs


class EpisodeViewSet(viewsets.ModelViewSet):
    """

    """
    model = Episode
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.action == 'retrieve':
                return EpisodeSerializer
            else:
                return EpisodeSerializer
        else:
            return EpisodeSerializer

    def get_form_object(self, subsId, pk):
        return get_object_or_404(Episode, channel_id=subsId, pk=pk)

    def get_queryset(self):
        """
        """
        subscription = self.kwargs.get('subsId')
        qs = self.model.objects.filter(channel_id=subscription).order_by("-id")
        return qs


class LanguagesViewset(viewsets.ReadOnlyModelViewSet):
    model = Language
    serializer_class = LanguagesSerializer

    def get_queryset(self):
        return self.model.objects.all()


class AddEpisodeView(APIView):
    def post(self, request, ):
        episode_id = request.data.get("episode_id")
        user_id = request.data.get("user_id")
        language = request.data.get("language")
        from datetime import datetime
        listened_time = request.data.get('listened_time', datetime.now())

        stat = ListenStats(episode_id=episode_id, listened_by_id=user_id, language=language,
                           listened_time=listened_time)
        stat.save()

        return Response(status=status.HTTP_201_CREATED)


class UpdateTranslationStatus(APIView):
    def post(self, request, episodeLanguageMappingId):
        mapping_status = request.data.get("status", "on-going")
        mapping_link = request.data.get("link", None)
        mapping_converted_title = request.data.get("converted_title", "")
        mapping_converted_text = request.data.get("converted_text", "")
        mapping_description = request.data.get("converted_description", "")

        mapping = EpisodeLanguageMapping.objects.get(id=episodeLanguageMappingId)
        mapping.status = mapping_status
        mapping.link = mapping_link
        mapping.converted_text = mapping_converted_text
        mapping.converted_title = mapping_converted_title
        mapping.description = mapping_description

        mapping.save()

        return Response(status=status.HTTP_201_CREATED)


def initiate_translation_request(mapping_id):
    print(mapping_id)
    mapping = EpisodeLanguageMapping.objects.get(id=mapping_id)
    original_translation = EpisodeLanguageMapping.objects.get(episode_id=mapping.episode_id, original=True)
    import requests
    import json
    headers = {
        "Content-Type": "application/json",
    }
    url = "https://24d02028.ngrok.io/start_pipeline"
    data = {
        "podcast_url": original_translation.link,
        "podcast_language": original_translation.language.label,
        "episode_id": mapping.episode.id,
        "language_mapping_id": mapping.id,
        "channel_id": mapping.episode.channel.id,
        "target_language": mapping.language.label,
        "title": original_translation.episode.title,
        "description": original_translation.description

    }
    try:
        r = requests.request('POST', url, headers=headers, data=json.dumps(data))
        print(r)
    except Exception as e:
        print(e)


class RequestTranslationStatus(APIView):
    def get(self, request, episodeId, languageId):

        mapping_exist = EpisodeLanguageMapping.objects.filter(language_id=languageId, episode_id=episodeId).count()
        if mapping_exist:
            if mapping_exist[0].status == "failed":
                initiate_translation_request(mapping_exist[0].id)
        else:
            mapping = EpisodeLanguageMapping(language_id=languageId, episode_id=episodeId, status="on going")
            mapping.save()
            initiate_translation_request(mapping.id)

        return Response(status=status.HTTP_201_CREATED)
