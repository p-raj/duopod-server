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


class ListenStats(models.Model):
    episode = models.ForeignKey(Episode, null=True, on_delete=models.SET_NULL)
    listened_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    language = models.CharField(_('Language listened in'), null=True, max_length=5)
    listened_time = models.DateTimeField(_('listened when'), auto_now_add=False, db_index=True)


class Language(models.Model):
    label = models.CharField(_('shorthand_form'), max_length=100)
    title = models.CharField(_('Full Name'), max_length=50)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class EpisodeLanguageMapping(models.Model):
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    episode = models.ForeignKey(Episode, null=True, on_delete=models.SET_NULL)
    link = models.TextField(_('Episode MP3 file link'), blank=True, null=True)
