# %%
from pydantic import BaseModel, EmailStr, HttpUrl, conint, constr
from typing import List, Dict

# %%

# List and Dict types with automatic parsing
class Product(BaseModel):
    name: str                       # Product name
    price: float                    # Automatically parses string to float
    tags: List[str]                 # List of tags, e.g. ["food", "fresh"]
    metadata: Dict[str, str]        # Dictionary with string keys and values

# Pydantic converts price from str to float automatically
pr1 = Product(name="apple", price="12.1", tags=["food"], metadata={"ID": "1"})
pr2 = Product(name="apple", price="12", tags=["food"], metadata={"ID": "1"})

# Notes:
# - List[str] will raise an error if a non-string element is passed.
# - Dict[str, str] enforces both keys and values to be strings.

# %%

# Email and URL validation with Pydantic's specialized types
class Contact(BaseModel):
    email: EmailStr                 # Validates format: something@domain.com
    website: HttpUrl                # Validates full URL (scheme + domain)

# Valid email and HTTPS URL
cnt1 = Contact(
    email="yasarserkan16@gmail.com",
    website="https://www.serkanyasar.dev"
)

# Notes:
# - If the email or URL is invalid, Pydantic will raise a ValidationError.
# - You can test by trying values like "abc" or "example.com" to see the error.

# %%

# Numeric and string constraints using conint and constr
class Person(BaseModel):
    age: conint(gt=0, lt=120)       # Must be > 0 and < 120
    name: constr(
        min_length=1,
        max_length=10,
        to_upper=True               # Converts name to uppercase automatically
    )

# Notes:
# - `conint` enforces numeric boundaries.
# - `constr` allows setting min/max length and string transformations like `.to_upper`.
# - If constraints are violated, ValidationError is raised.

# %%
