# %%
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
import json

# %%
# 1. Custom JSON encoder for UUID and datetime
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {
            UUID: lambda v: str(v),
            datetime: lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S')
        }

user = User(name="Serkan")
print("Custom JSON:", user.model_dump_json(indent=2))

# %%
# 2. Overriding model_dump method (advanced)
class Product(BaseModel):
    name: str
    price: float
    internal_code: str

    def model_dump(self, **kwargs):
        base = super().model_dump(**kwargs)
        base["price_with_tax"] = round(self.price * 1.2, 2)
        return base

p = Product(name="Mouse", price=100, internal_code="XYZ123")
print("Custom model_dump with tax:", p.model_dump())

# %%
# 3. Hiding fields from serialization
class SecureUser(BaseModel):
    username: str
    password: str  # Do not expose

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        data.pop("password", None)
        return data

su = SecureUser(username="admin", password="secret123")
print("Safe output:", su.model_dump())

# %%
# 4. Conditional serialization with `exclude` or `include`
class Blog(BaseModel):
    title: str
    content: str
    is_published: bool
    views: int

blog = Blog(title="Hello", content="World", is_published=False, views=100)

# Export only selected fields
print("Only title:", blog.model_dump(include={"title"}))

# Exclude specific fields
print("Without views:", blog.model_dump(exclude={"views"}))

# %%
