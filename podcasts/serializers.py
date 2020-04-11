from rest_framework import serializers

from podcasts.models import Subscription, Episode


class SubscriptionSerializer(serializers.ModelSerializer):
    """

    """
    name = serializers.ReadOnlyField()
    creator = serializers.ReadOnlyField(source='creator.get_full_name')

    class Meta:
        model = Subscription
        exclude = ()


class EpisodeSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Episode
        fields = '__all__'
