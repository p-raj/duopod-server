from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter

from podcasts.analytics.api import ListenrStatsViewSet
from podcasts.views import SubscriptionViewSet, EpisodeViewSet, LanguagesViewset, UserSubscriptionViewSet, \
    AddEpisodeView, UpdateTranslationStatus, RequestTranslationStatus

router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet, base_name='subscriptions')
router.register(r'user/(?P<userId>\d+?)/subscriptions', UserSubscriptionViewSet, base_name='user_subscriptions')
router.register(r'subscriptions/(?P<subsId>\d+?)/episodes',
                EpisodeViewSet,
                base_name='episodes')
router.register('languages', LanguagesViewset, base_name='languages')

router.register(r'creator/(?P<userId>\d+?)/listenerStats',
                ListenrStatsViewSet,
                base_name='listenerStats')

urlpatterns = [
    path("add-episode-view/", AddEpisodeView.as_view(), name="add-episode-view"),
    url(r'^update-language-translation/(?P<episodeLanguageMappingId>\d+?)/$',
        UpdateTranslationStatus.as_view(),
        name='update-language-translation'),
    url(r'^request-language-translation/(?P<episodeId>\d+?)/language/(?P<languageId>\d+?)/$',
        RequestTranslationStatus.as_view(),
        name='update-language-translation')
]

urlpatterns += router.urls
