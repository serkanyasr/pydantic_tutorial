# %%
from pydantic import BaseModel

# %%

# Basic Pydantic model with standard Python types
class User(BaseModel):
    Id: int               # Integer field (capitalized field names are allowed but not recommended by convention)
    name: str             # String field
    age: int              # Integer field
    is_active: bool       # Boolean field

# %%

# Pydantic automatically parses and converts compatible types.

# int → int, str → str, bool ← int (0 → False)
user1 = User(Id=1, name="Serkan", age=25, is_active=0)

# str "False" is converted to boolean False
user2 = User(Id=1, name="Serkan", age=25, is_active="False")

# str "25" is parsed to int → valid
user3 = User(Id=1, name="Serkan", age="25", is_active=False)

# str "25" → int, str "0" → bool False
user4 = User(Id=1, name="Serkan", age="25", is_active="0")

# You can print the parsed models to see what types are actually stored
print(user1)
print(user2)
print(user3)
print(user4)

# %%
