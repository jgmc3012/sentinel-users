"""Phone models"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Phone(models.Model):
    number = PhoneNumberField(_("Phone number"), blank=False, help_text='Contact phone number')
    main = models.BooleanField(_("Main phone"), default=False)
    user = models.ForeignKey(
        'users.User', blank=False, verbose_name=_("User own"),
        on_delete=models.CASCADE
    )
