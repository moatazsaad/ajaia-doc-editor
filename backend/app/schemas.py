from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    email: str
    name: str

    class Config:
        from_attributes = True


class DocumentCreate(BaseModel):
    title: str = "Untitled Document"
    owner_id: int


class DocumentUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class DocumentOut(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    class Config:
        from_attributes = True


class ShareRequest(BaseModel):
    email: str