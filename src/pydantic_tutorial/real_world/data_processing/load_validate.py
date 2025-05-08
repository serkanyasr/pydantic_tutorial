
from pydantic import BaseModel, ValidationError, conint, EmailStr
from typing import List
import json

# Define the schema for a single user record
class UserData(BaseModel):
    name: str  # Name of the user
    age: conint(gt=0)  # type: ignore # Age must be a positive integer
    email: EmailStr  # Must be a valid email address
    is_active: bool = True  # Optional field, default is True

# Sample raw data (could come from a file, API, etc.)
raw_data = '''
[
    {"name": "Alice", "age": 30, "email": "alice@example.com", "is_active": true},
    {"name": "Bob", "age": -5, "email": "bob[at]example.com", "is_active": false},
    {"name": "Charlie", "age": 22, "email": "charlie@example.com"}
]
'''

# Parse JSON string into Python objects
data = json.loads(raw_data)  # Load raw JSON data

valid_users: List[UserData] = []  # List to store validated user data
errors = []  # List to store any validation errors

for i, record in enumerate(data):
    try:
        user = UserData(**record)  # Validate and parse record
        valid_users.append(user)
    except ValidationError as e:
        print(f"Validation error for record {i}:")
        print(e)
        errors.append((i, e))

# Print results
print("\nValid users:")
for user in valid_users:
    print(user)

print("\nNumber of validation errors:", len(errors))
