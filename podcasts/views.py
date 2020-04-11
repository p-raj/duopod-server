from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from podcasts.models import Subscription, Episode, Language
from podcasts.serializers import SubscriptionSerializer, EpisodeSerializer, LanguagesSerializer
from rest_framework.response import Response

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
        qs = self.model.objects.filter(channel_id= subscription).order_by("-id")
        return qs


class LanguagesViewset(viewsets.ReadOnlyModelViewSet):
    model = Language
    serializer_class = LanguagesSerializer

    def get_queryset(self):
        return self.model.objects.all()
