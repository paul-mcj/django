from django.shortcuts import render, redirect
from .models import Room, Message
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {"id": 1, "name": "Python Tutorials", "desc": "lets learn the basics of this cool language"},
#     {"id": 2, "name": "Learn JavaScript", "desc": "JS is important for web development"},
#     {"id": 3, "name": "All backend stuff right here!!", "desc": "mysql, mongodb, apis and much more!"},
# ]

def home(req):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(req, "base/home.html", context)

def room(req, primary_key):
    room = Room.objects.get(id=primary_key)
    messages = Message.objects.filter(room=primary_key)
    context = {"room": room, "messages": messages}
    return render(req, "base/room.html", context)

def createRoom(req):
    form = RoomForm()
    if(req.method == "POST"):
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(req, "base/room_form.html", context)