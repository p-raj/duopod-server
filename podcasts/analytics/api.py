from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from podcasts.analytics.serializers import ListenStatsSerializer
from podcasts.models import ListenStats
from podcasts.analytics.filters import *

class ListenrStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """Handles Upload Members

    """
    model = ListenStats
    pagination_class = LimitOffsetPagination
    serializer_class = ListenStatsSerializer

    filter_backends = (SubscriptionFilterBackend,EpisodeFilterBackend, ListenedTmeFilterBackend
        )

    def get_queryset(self):
        """

        :return: MemberBook Queryset
        """
        creator = self.kwargs.get('userId')
        qs = self.model.objects.filter(episode__channel__creator_id=creator).order_by("-id")
        return qs
