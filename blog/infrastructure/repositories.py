from typing import List, Optional
from ..domain.entities import PostEntity
from ..domain.interfaces import IPostRepository
from ..models import Post

class DjangoPostRepository(IPostRepository):
    def to_entity(self, model: Post) -> PostEntity:
        return PostEntity(
            id=model.id,
            title=model.title,
            content=model.content,
            author_id=model.author.id,
            slug=model.slug,
            image=model.image.name if model.image else None,
            published=model.published,
            created_at=model.created_at,
            updated_at=model.updated_at
        )

    def create(self, post: PostEntity) -> PostEntity:
        # Note: image handling might need adjustment depending on how it's passed (string path vs UploadedFile)
        # For now assuming it's handled by view/serializer before reaching here or simplistically
        model = Post.objects.create(
            title=post.title,
            content=post.content,
            author_id=post.author_id,
            slug=post.slug,
            published=post.published
            # Image is tricky in pure clean arch without passing file objects, will handle simply for now
        )
        if post.image:
             model.image = post.image
             model.save()
        return self.to_entity(model)

    def get_by_slug(self, slug: str) -> Optional[PostEntity]:
        try:
            model = Post.objects.get(slug=slug)
            return self.to_entity(model)
        except Post.DoesNotExist:
            return None

    def list(self) -> List[PostEntity]:
        # Using select_related for performance, though strictly implementation detail
        models = Post.objects.all().select_related('author').order_by('-created_at')
        return [self.to_entity(m) for m in models]

    def update(self, post: PostEntity) -> PostEntity:
        # Not fully implemented in this MVP refactor step but required by interface
        pass

    def delete(self, slug: str) -> None:
        Post.objects.filter(slug=slug).delete()

    def slug_exists(self, slug: str) -> bool:
        return Post.objects.filter(slug=slug).exists()
