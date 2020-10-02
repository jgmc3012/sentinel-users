from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class User(AbstractUser):
    """Default user for sentinel users."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    country = CountryField()

    REQUIRED_FIELDS = ['email', 'country']

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})
