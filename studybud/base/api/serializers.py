from base.models import Room, Message, Topic
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User # User objects without explicit fields defined (or without exceptions) gives passwords and other confidential info away
        fields = ["username", "email", "date_joined", "groups"]