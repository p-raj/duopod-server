from rest_framework.routers import DefaultRouter

from podcasts.views import SubscriptionViewSet, EpisodeViewSet

router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet, base_name='subscriptions')
router.register(r'subscriptions/(?P<subsId>\d+?)/episodes',
                EpisodeViewSet,
                base_name='episodes')

urlpatterns = [

]

urlpatterns += router.urls
