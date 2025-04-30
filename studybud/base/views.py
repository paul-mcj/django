from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RoomForm
from .models import Room, Topic, Message
# Create your views here.

# rooms = [
#     {"id": 1, "name": "Python Tutorials", "desc": "lets learn the basics of this cool language"},
#     {"id": 2, "name": "Learn JavaScript", "desc": "JS is important for web development"},
#     {"id": 3, "name": "All backend stuff right here!!", "desc": "mysql, mongodb, apis and much more!"},
# ]

def loginPage(req):
    page = "login"

    if req.user.is_authenticated:
        return redirect("home")

    if req.method == "POST":
        username = req.POST.get("username").lower()
        password = req.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(req, "User does not exist")
            return redirect("login")
        
        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect("home")
        else:
            messages.error(req, "Username OR password incorrect")

    context = {"page": page}
    return render(req, "base/login_register.html", context)

def logoutUser(req):
    # django logout method will automatically delete the session token which validates the user
    logout(req)
    return redirect("home")

def registerPage(req):
    form = UserCreationForm()
    context = {"form": form}

    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False) # don't add to backend just yet, lets quickly update username first to meet our standards
            user.username = user.username.lower()
            user.save()
            login(req, user)
            return redirect("home")
        else:
            messages.error(req, "An error occurred during registration")

    return render(req, "base/login_register.html", context)

def home(req):
    q = req.GET.get("q") if req.GET.get("q") != None else ""
    # search params can be for topic, name of room, or description of room 
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(desc__icontains=q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "topics": topics, "room_count": room_count}
    return render(req, "base/home.html", context)

def room(req, primary_key):
    room = Room.objects.get(id=primary_key)
    messages = Message.objects.filter(room=primary_key)
    context = {"room": room, "messages": messages}
    return render(req, "base/room.html", context)

@login_required(login_url="login")
def createRoom(req):
    form = RoomForm()
    if(req.method == "POST"):
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(req, "base/room_form.html", context)

@login_required(login_url="login")
def updateRoom(req, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if req.user != room.host:
        return HttpResponse("Authentication required")

    if req.method == "POST":
        form = RoomForm(req.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    context = {"form":form}
    return render(req, "base/room_form.html", context)

@login_required(login_url="login")
def deleteRoom(req, pk):
    room = Room.objects.get(id=pk)

    if req.user != room.host:
        return HttpResponse("Authentication required")
    
    if req.method == "POST":
        room.delete()
        return redirect("home")
    return render(req, "base/delete.html", {"obj": room})