from rest_framework import serializers

from podcasts.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """

    """
    name = serializers.ReadOnlyField()
    creator = serializers.ReadOnlyField(source='creator.id')

    class Meta:
        model = Subscription
        exclude = ()
