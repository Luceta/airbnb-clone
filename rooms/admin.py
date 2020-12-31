from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """item admin definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Model Definition """


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass