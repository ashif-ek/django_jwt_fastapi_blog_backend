from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    Public endpoint to create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for posts.
    Auth required for create/update/delete.
    """
    queryset = Post.objects.all().select_related("author")
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
