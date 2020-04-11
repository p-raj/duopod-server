from django.urls import path
from rest_framework.routers import DefaultRouter

from podcasts.views import SubscriptionViewSet, EpisodeViewSet, LanguagesViewset

router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet, base_name='subscriptions')
router.register(r'subscriptions/(?P<subsId>\d+?)/episodes',
                EpisodeViewSet,
                base_name='episodes')
router.register('languages', LanguagesViewset, base_name='languages')

urlpatterns = [

]

urlpatterns += router.urls
