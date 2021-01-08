from django.shortcuts import render
from . import models
from math import ceil

# Create your views here.

# template 네임과 return html 이름 동일 해야함
# view name 은 urls.py파일에 있는 이름과 같아야함 all_rooms
# template에서 context변수와 같아야함.


def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page * page_size
    offset = limit - page_size
    page_count = ceil(models.Room.objects.count() / 10)
    print(page_count)
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(0, page_count),
        },
    )
