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

    def create(self, request, *args, **kwargs):
        from .infrastructure.repositories import DjangoPostRepository
        from .application.services import PostService
        from rest_framework.response import Response
        from rest_framework import status

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repo = DjangoPostRepository()
        service = PostService(repo)

        # Call Service
        post_entity = service.create_post(
            title=serializer.validated_data.get('title'),
            content=serializer.validated_data.get('content'),
            author_id=request.user.id,
            image=serializer.validated_data.get('image'),
            published=serializer.validated_data.get('published', True)
        )

        # Refetch for standard DRF response
        # In a purer clean arch, we would return a DTO, but here we reuse the Serializer
        # which expects a model instance.
        instance = Post.objects.get(slug=post_entity.slug)
        serializer = self.get_serializer(instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Note: perform_create is no longer used for the actual creation logic
    # but kept if any other mixins rely on it (though we overrode create entirely).
    def perform_create(self, serializer):
        pass
