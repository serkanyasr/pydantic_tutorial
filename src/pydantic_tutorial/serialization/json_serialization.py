# %%
from pydantic import BaseModel, ValidationError
from typing import List
from datetime import datetime
import json

# %%
# 1. Basic model
class User(BaseModel):
    id: int
    name: str
    tags: List[str]
    joined_at: datetime

# %%
user = User(id=1, name="Serkan", tags=["admin", "dev"], joined_at=datetime.now())

# %%
# 2. Serialization - model to dict
print("To dict:", user.model_dump())  # Pydantic v2 (.dict() in v1)

# %%
# 3. Serialization - model to JSON string
print("To JSON:", user.model_dump_json(indent=2))  # (.json(indent=2) in v1)

# %%
# 4. Manual JSON encode (alternative)
json_str = json.dumps(user.model_dump(), indent=2, default=str)
print("Manual JSON:", json_str)

# %%
# 5. Deserialization - from dict
data = {
    "id": 2,
    "name": "Serkan",
    "tags": ["editor"],
    "joined_at": "2024-10-01T10:00:00"
}

user2 = User.model_validate(data)  # parse_obj in v1
print("From dict:", user2)

# %%
# 6. Nested structures
class Blog(BaseModel):
    title: str
    author: User
    created_at: datetime

blog = Blog(title="Pydantic Serialization", author=user, created_at=datetime.now())

print("Nested JSON:", blog.model_dump_json(indent=2))

# %%
# 7. Deserialization of nested structure
blog_data = {
    "title": "Nested Example",
    "author": {
        "id": 3,
        "name": "Serkan",
        "tags": ["writer"],
        "joined_at": "2023-06-01T08:30:00"
    },
    "created_at": "2024-12-31T23:59:59"
}

blog_obj = Blog.model_validate(blog_data)
print(blog_obj)

# %%
