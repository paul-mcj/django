from base.models import Room, Message, Topic
from django.contrib.auth.models import User
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .serializers import RoomSerializer, MessageSerializer, TopicSerializer, UserSerializer

@api_view(["GET"])
def getRoutes(req):
    routes = ["GET /api", "GET /api/rooms", "GET /api/rooms/:id"]
    return Response(routes)

@api_view(["GET"])
def getRooms(req): 
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getSingleRoom(req, id):
    room = Room.objects.get(id=id)
    serializer = RoomSerializer(room)

    return Response(serializer.data)

@api_view(["GET"])
def getRoomMessages(req, id):
    room = Room.objects.get(id=id)
    messages = Message.objects.filter(room=room)

    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getTopics(req):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getUsers(req):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getSingleUser(req, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)

    return Response(serializer.data)

@api_view(["PUT"])
def updateSingleUser(req, id):
    