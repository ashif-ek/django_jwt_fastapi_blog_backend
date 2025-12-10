from django.utils.text import slugify
from typing import List, Optional
from ..domain.entities import PostEntity
from ..domain.interfaces import IPostRepository

class PostService:
    def __init__(self, repository: IPostRepository):
        self.repository = repository

    def create_post(self, title: str, content: str, author_id: int, image: Optional[str] = None, published: bool = True) -> PostEntity:
        base_slug = slugify(title)[:50]
        slug = base_slug
        counter = 1
        while self.repository.slug_exists(slug):
            slug = f"{base_slug}-{counter}"
            counter += 1
        
        post = PostEntity(
            title=title,
            content=content,
            author_id=author_id,
            slug=slug,
            image=image,
            published=published
        )
        return self.repository.create(post)

    def list_posts(self) -> List[PostEntity]:
        return self.repository.list()

    def get_post(self, slug: str) -> Optional[PostEntity]:
        return self.repository.get_by_slug(slug)
