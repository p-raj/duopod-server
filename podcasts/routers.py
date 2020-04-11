"""
version v4 router endpoints views
"""
from rest_framework.routers import SimpleRouter

from podcasts.views import SubscriptionViewSet

router = SimpleRouter()

router.register(r'subscriptions',
                SubscriptionViewSet,
                base_name='subscriptions')

urlpatterns = [

]

urlpatterns += router.urls

app_name = "podcast"
