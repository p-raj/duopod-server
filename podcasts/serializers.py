from rest_framework import serializers

from podcasts.models import Subscription, Episode, Language


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
    languages = serializers.SerializerMethodField()

    def get_languages(self, instance):
        return instance.episodelanguagemapping_set.values('language__label', 'link', 'converted_title', 'converted_text')

    class Meta:
        model = Episode
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
