from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import LoginView

router = DefaultRouter()

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),

]

urlpatterns += router.urls
