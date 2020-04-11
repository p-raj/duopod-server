from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from podcasts.models import Subscription
from podcasts.serializers import SubscriptionSerializer


# class SubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
#     """Handles Upload Members
#
#     """
#     model = Subscription
#     pagination_class = LimitOffsetPagination
#     serializer_class = SubscriptionSerializer
#
#     def get_queryset(self):
#         """
#
#         :return: MemberBook Queryset
#         """
#
#         qs = self.model.objects.order_by("-id")
#         return qs


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
