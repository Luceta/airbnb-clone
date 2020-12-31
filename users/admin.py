from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# admin.py 에  models가져오려면 decorate해주기
# admin.site.register(models.User, CustomUserAdmin) 과 동일
# list display , list filter개념 admin외부 보여주는 것


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ custom User Admin """

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
