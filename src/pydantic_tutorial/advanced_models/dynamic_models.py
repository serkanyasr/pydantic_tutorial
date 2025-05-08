# %%
from pydantic import BaseModel, create_model, ValidationError, Field, EmailStr
from typing import Optional

# %%
# 1. Basic dynamic model creation
DynamicUser = create_model(
    'DynamicUser',
    username=(str, ...),           # required
    age=(int, Field(..., ge=0)),   # required with constraint
    email=(Optional[EmailStr], None)  # optional with default None
)

# Usage
user = DynamicUser(username="serkan", age=25, email="serkan@example.com")
print(user)

# %%
# 2. Missing required field (will raise error)
try:
    invalid_user = DynamicUser(username="serkan")
except ValidationError as e:
    print("Validation Error:\n", e)

# %%
# 3. Dynamic model with default values
DynamicProduct = create_model(
    'DynamicProduct',
    name=(str, ...),
    price=(float, Field(default=0.0, ge=0)),
    in_stock=(bool, True)
)

product = DynamicProduct(name="Keyboard")
print(product)

# %%
# 4. Base + dynamic fields (inherit from BaseModel)
class BaseEntity(BaseModel):
    id: int

DynamicEmployee = create_model(
    'DynamicEmployee',
    name=(str, ...),
    salary=(float, Field(..., gt=0)),
    __base__=BaseEntity
)

employee = DynamicEmployee(id=1, name="Ahmet", salary=3000)
print(employee)