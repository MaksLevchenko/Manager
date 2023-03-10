from django.contrib import admin

from Client_Manager.models import Client, Comment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
