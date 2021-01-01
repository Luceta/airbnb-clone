from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ("__str__", "created")  # from timpe stampe model created 가져옴


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    list_display = ("__str__", "count_messages", "count_participants")


# Register your models here.
