from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField("título", max_length=180)
    slug = models.SlugField(unique=True)
    body = models.TextField("texto")
    media = models.FileField("archivo multimedia", upload_to="posts/%Y/%m/", blank=True)
    published_at = models.DateTimeField("fecha de publicación", default=timezone.now)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField("nombre", max_length=80)
    body = models.TextField("comentario", max_length=1000)
    created_at = models.DateTimeField("fecha", auto_now_add=True)
    approved = models.BooleanField("aprobado", default=False)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"

    def __str__(self):
        return f"{self.name}: {self.post.title}"