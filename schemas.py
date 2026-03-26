from pydantic import BaseModel

# Used for creating book
class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    quantity: int

# Used for response
class Book(BookCreate):
    id: int

    class Config:
        from_attributes = True   # (important for SQLAlchemy)