from rest_framework import serializers

from .models import Messages


class MessageSerializer(serializers.ModelSerializer):
    user_permission = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Messages
        fields = "__all__"
