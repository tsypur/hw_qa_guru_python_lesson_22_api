from pydantic import BaseModel, Field
from typing import List, Optional


class Pet(BaseModel):

    id: Optional[int] = None
    name: str
    photoUrls: List[str] = []
    status: Optional[str] = None

    @classmethod
    def create_request(cls, name: str, photo_urls: List[str] = None, status: str = "available"):

        if photo_urls is None:
            photo_urls = []
        return cls(name=name, photoUrls=photo_urls, status=status).dict(exclude_none=True)


class Order(BaseModel):

    id: Optional[int] = None
    petId: Optional[int] = Field(None, ge=1)
    quantity: Optional[int] = Field(1, ge=1, le=100)
    status: Optional[str] = Field(None, regex="^(placed|approved|delivered)$")
    complete: Optional[bool] = False

    @classmethod
    def create_request(cls, pet_id: int, quantity: int = 1,
                       status: str = "placed", complete: bool = False):

        return cls(petId=pet_id, quantity=quantity, status=status, complete=complete).dict(exclude_none=True)