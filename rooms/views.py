from django.urls import reverse
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models

# template 네임과 return html 이름 동일 해야함
# view name 은 urls.py파일에 있는 이름과 같아야함 all_rooms
# template에서 context변수와 같아야함.


class HomeView(ListView):
    pass
    """home detailed view"""
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = "page"
    context_object_name = "rooms"


"""
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()"""


class RoomDetail(DetailView):
    model = models.Room
