from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at")
    list_filter = ("published_at",)
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "created_at", "approved")
    list_filter = ("approved", "created_at")
    list_editable = ("approved",)
    search_fields = ("name", "body", "post__title")