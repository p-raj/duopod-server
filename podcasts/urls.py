from rest_framework.routers import DefaultRouter

from podcasts.views import SubscriptionViewSet

router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet, base_name='subscriptions')

urlpatterns = [

]

urlpatterns += router.urls
