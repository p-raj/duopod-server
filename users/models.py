from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

SUBSCRIBER = 1
CREATOR = 2

USER_TYPE = (
    (CREATOR, _("creator")),
    (SUBSCRIBER, _("subscriber")),
)


class UserType(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    type = models.IntegerField(_("User Type"), choices=USER_TYPE, default=SUBSCRIBER)
