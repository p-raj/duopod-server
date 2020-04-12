from rest_framework import serializers

from podcasts.models import ListenStats


class ListenStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListenStats
        fields = '__all__'
