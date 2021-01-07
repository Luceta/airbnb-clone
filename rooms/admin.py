from django.contrib import admin

# from django.utils.html import mark_safe 2version
from django.utils.safestring import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """item admin definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):
    model = models.Photo


class Roominline(admin.TabularInline):
    model = models.Room


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Model Definition """

    # 인라인 모델 admin 안에 또 다른 admin은 넣는 법 stacked in line and tabular inline
    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "price",
        "description",
        "country",
        "city",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("price",)

    list_filter = (
        "instant_book",
        "host__superhost",  # __ 2번으로 superhost를 필터링
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    # 호스트를 검색하게해줘 user admin을 통해
    raw_id_fields = ("host",)
    # 외부 서치바
    search_fields = ("=city", "^host__username")

    filter_horizontal = ("amenities", "facilities", "house_rules")

    # roomadmin 이 self, obj는 row를 받음 이함수를 리스트에 넣음으로 정렬에 갯수 표시가능
    def count_amenities(self, obj):
        return obj.amenities.count()
        # count_amenities.short_descrtiption = " "이렇게 함으로써 컬럼명도 변경 가능

    count_amenities.short_description = "Amenity Count"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):

        return mark_safe(f'<img width= "60px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
