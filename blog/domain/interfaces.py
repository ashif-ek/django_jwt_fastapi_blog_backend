from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import PostEntity

class IPostRepository(ABC):
    @abstractmethod
    def create(self, post: PostEntity) -> PostEntity:
        pass

    @abstractmethod
    def get_by_slug(self, slug: str) -> Optional[PostEntity]:
        pass

    @abstractmethod
    def list(self) -> List[PostEntity]:
        pass

    @abstractmethod
    def update(self, post: PostEntity) -> PostEntity:
        pass

    @abstractmethod
    def delete(self, slug: str) -> None:
        pass
    
    @abstractmethod
    def slug_exists(self, slug: str) -> bool:
        pass
