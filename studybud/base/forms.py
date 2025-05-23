from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "bio", "avatar"]
    
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]