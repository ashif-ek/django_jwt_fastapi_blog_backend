from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "image",
            "slug",
            "content",
            "author",
            "author_username",
            "published",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "slug", "author", "author_username", "created_at", "updated_at"]
