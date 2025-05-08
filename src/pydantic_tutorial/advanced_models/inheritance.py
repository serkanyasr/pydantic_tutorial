# %%
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# %%
# 1. Base model (used for reusability)
class UserBase(BaseModel):
    username: str
    email: str

# 2. Inherited model with additional fields
class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool

# Usage
create_data = UserCreate(username="serkan", email="serkan@example.com", password="secure123")
read_data = UserRead(username="serkan", email="serkan@example.com", id=1, is_active=True)

print(create_data)
print(read_data)

# %%
# 3. Field override example
class AdminUser(UserRead):
    is_active: bool = Field(default=True)
    admin_level: int = Field(default=1, ge=1, le=5)

# Usage
admin = AdminUser(
    username="admin",
    email="admin@example.com",
    id=99,
    is_active=False,
    admin_level=3
)
print(admin)

# %%
# 4. Mixin class example (reusable timestamp fields)
class TimestampMixin(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

# Inherit mixin + model
class Product(TimestampMixin, BaseModel):
    name: str
    price: float

product = Product(name="Laptop", price=1500.00)
print(product)

# %%
# (Optional) 5. Base + Type Hint Switching (not true polymorphism)
class Animal(BaseModel):
    name: str

class Dog(Animal):
    breed: str

class Cat(Animal):
    color: str

def print_animal_info(animal: Animal):
    print(f"Animal: {animal.name}")

dog = Dog(name="Rex", breed="Labrador")
cat = Cat(name="Misty", color="Gray")

print_animal_info(dog)
print_animal_info(cat)

# %%
