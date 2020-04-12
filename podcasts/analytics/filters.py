import datetime

import django_filters.rest_framework
from rest_framework.exceptions import ValidationError


class SubscriptionFilterBackend(django_filters.rest_framework.DjangoFilterBackend):
    """Enable Filter by
        -  Gatekeeper

    """

    def filter_queryset(self, request, queryset, view):
        if 'subscription' in request.query_params:
            try:
                queryset = queryset.filter(episode__channel__id=int(request.query_params.get('subscription')))
            except ValidationError as e:
                pass

        return queryset


class EpisodeFilterBackend(django_filters.rest_framework.DjangoFilterBackend):
    """Enable Filter by
        -  Activity Type

    """

    def filter_queryset(self, request, queryset, view):
        if 'episode' in request.query_params:
            try:
                queryset = queryset.filter(episode_id=int(request.query_params.get('episode')))
            except ValidationError as e:
                pass

        return queryset


class ListenedTmeFilterBackend(django_filters.rest_framework.DjangoFilterBackend):
    """
    Default time will be a 1 day
    """

    def filter_queryset(self, request, queryset, view):

        if 'listened_time_gt' in request.query_params and 'listened_time_lt' in request.query_params:
            try:
                queryset = queryset.filter(
                    listened_time__range=(
                        request.query_params.get('listened_time_gt'), request.query_params.get('listened_time_lt')))
            except ValidationError as e:
                pass

        return queryset
