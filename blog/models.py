from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_at"]

    # Logic moved to Service Layer in Clean Architecture
    # def save(self, *args, **kwargs):
    #     if not self.slug: ...
    #     super().save(*args, **kwargs)
    pass

    def __str__(self):
        return f"{self.title} by {self.author.username}"
