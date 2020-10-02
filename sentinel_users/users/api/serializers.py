from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id", "is_staff", "is_active", "date_joined", "groups",
                   "user_permissions", "is_superuser", "last_login", "password"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "email": {"required": True, "allow_null": False},
            "first_name": {"required": True, "allow_null": False},
            "last_name": {"required": True, "allow_null": False},
        }
