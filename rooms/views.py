from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models
from math import ceil

# Create your views here.

# template 네임과 return html 이름 동일 해야함
# view name 은 urls.py파일에 있는 이름과 같아야함 all_rooms
# template에서 context변수와 같아야함.


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
