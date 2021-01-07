from django.shortcuts import render
from . import models

# Create your views here.

# template 네임과 return html 이름 동일 해야함
# view name 은 urls.py파일에 있는 이름과 같아야함 all_rooms
# template에서 context변수와 같아야함.


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
