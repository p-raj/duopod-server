from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Subscription(models.Model):
    name = models.TextField(_('Subscription Name'), blank=True, null=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Episode(models.Model):
    channel = models.ForeignKey(Subscription, null=True, on_delete=models.SET_NULL)
    title = models.TextField(_('Episode Title'), blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), null=True, auto_now_add=True)
    duration = models.PositiveIntegerField(_('Episode duration'), null=True)
