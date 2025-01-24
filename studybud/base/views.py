from django.shortcuts import render

# Create your views here.

rooms = [
    {"id": 1, "name": "Python Tutorials", "desc": "lets learn the basics of this cool language"},
    {"id": 2, "name": "Learn JavaScript", "desc": "JS is important for web development"},
    {"id": 3, "name": "All backend stuff right here!!", "desc": "mysql, mongodb, apis and much more!"},
]

def home(req):
    context = {"rooms": rooms}
    return render(req, "base/home.html", context)

def room(req, primary_key):
    room = None
    for i in rooms:
        if i["id"] == int(primary_key):
            room = i
    context = {"room": room}
    return render(req, "base/room.html", context)