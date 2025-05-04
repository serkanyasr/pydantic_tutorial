# %%
from pydantic import BaseModel, Field, ValidationError, computed_field
from typing import Optional
# %%

# Basic Pydantic model with required and optional fields
class BlogPost(BaseModel):
    title: str                                # required field
    content: Optional[str] = None             # optional field with default = None
    views: int = 0                            # optional with default value
    published: bool = Field(default=False)    # explicit default with Field()

# Model instance creation with type coercion (str "25" → int 25)
pst1 = BlogPost(
    title="title",
    content="content",
    views="25",        # Will be parsed to integer
    published=True
)

# %%

# Field constraints using Field()
class Account(BaseModel):
    username: str = Field(..., min_length=4, max_length=12)
    balance: float = Field(..., gt=0)

# Creating a valid Account instance
act = Account(username="Serkan", balance=10)

# %%

# Error handling with ValidationError
try:
    post = BlogPost(title="Pydantic Tutorial", views=-5)
except ValidationError as e:
    print(e)


# %%

# Using aliases and computed fields
class User(BaseModel):
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Config:
        populate_by_name = True   # Allows usage of field names or aliases when creating objects

# Example using alias fields
user = User(firstName="Serkan", lastName="Yaşar")
print(user.full_name)  # Output: Serkan Yaşar

# %%
