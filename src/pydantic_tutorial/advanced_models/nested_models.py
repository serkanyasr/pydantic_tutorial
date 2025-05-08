# %%
from pydantic import BaseModel
from typing import List, Optional, Dict

# %%
# 1. Simple Nested Model
class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class User(BaseModel):
    id: int
    name: str
    address: Address

# Usage
user = User(
    id=1,
    name="Serkan",
    address={
        "street": "Main St",
        "city": "Istanbul",
        "zipcode": "34000"
    }
)
print(user)
# %%
user = User(
    id=32, 
    name="Serkan", 
    address=Address(
        street="street",
        city="Kahramanmaras",
        zipcode="46"
    )
)


# %%
# 2. Nested Model with List[Model]
class Item(BaseModel):
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    order_id: int
    items: List[Item]   # List of nested models
    customer: User      # Re-using previous User model

# Usage
order = Order(
    order_id=1001,
    items=[
        {"name": "Apple", "quantity": 3, "price": 5.0},
        {"name": "Banana", "quantity": 2, "price": 3.5}
    ],
    customer=user
)
print(order)
# %%
order1 = Order(
    order_id=12,
    items = [
        Item(name="apple" , quantity=3 ,price=3.5),
    ],
    customer=user
)
print(order1)
# %%
# 3. Optional Nested Model
class Profile(BaseModel):
    bio: Optional[str] = None
    website: Optional[str] = None

class ExtendedUser(BaseModel):
    username: str
    email: str
    profile: Optional[Profile] = None

# Usage
user_with_profile = ExtendedUser(
    username="serkan",
    email="serkan@example.com",
    profile={"bio": "Backend Developer", "website": "https://serkanyasar.dev"}
)
print(user_with_profile)

user_without_profile = ExtendedUser(
    username="guest",
    email="guest@example.com"
)
print(user_without_profile)


# %%
# 5. Deeply Nested Structure (Dictionary of Models)
class Department(BaseModel):
    name: str
    employees: List[User]

class Company(BaseModel):
    name: str
    departments: Dict[str, Department]

# Usage
company = Company(
    name="TechCorp",
    departments={
        "IT": {
            "name": "IT",
            "employees": [
                {"id": 1, "name": "Serkan", "address": {"street": "Main", "city": "Istanbul", "zipcode": "34000"}},
                {"id": 2, "name": "Elif", "address": {"street": "Side", "city": "Bursa", "zipcode": "16000"}}
            ]
        }
    }
)
print(company)