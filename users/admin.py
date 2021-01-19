from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms.admin import Roominline

# admin.py 에  models가져오려면 decorate해주기
# admin.site.register(models.User, CustomUserAdmin) 과 동일
# list display , list filter개념 admin외부 보여주는 것


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ custom User Admin """

    inlines = (Roominline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "profile_pic",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret_code",
    )