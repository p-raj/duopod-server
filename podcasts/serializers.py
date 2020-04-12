from rest_framework import serializers

from podcasts.models import Subscription, Episode, Language


class SubscriptionSerializer(serializers.ModelSerializer):
    """

    """
    name = serializers.ReadOnlyField()
    creator = serializers.ReadOnlyField(source='creator.get_full_name')
    episodes = serializers.SerializerMethodField()

    def get_episodes(self, instance):
        return instance.episode_set.count()

    class Meta:
        model = Subscription
        exclude = ()


class EpisodeSerializer(serializers.ModelSerializer):
    """

    """
    languages = serializers.SerializerMethodField()
    creator = serializers.SerializerMethodField()

    def get_languages(self, instance):
        return instance.episodelanguagemapping_set.values('language__label', 'link', 'converted_title', 'converted_text', 'status', 'original', 'description')

    def get_creator(self, instance):
        return instance.channel.creator.get_full_name()

    class Meta:
        model = Episode
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
