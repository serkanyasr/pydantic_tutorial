from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

# Input data model
class UserInput(BaseModel):
    name: str  # Raw name from source
    email: EmailStr
    signup_timestamp: str  # String timestamp (e.g. "2024-05-08 12:34:00")

# Output data model after transformation
class UserTransformed(BaseModel):
    name_upper: str  # Transformed name in uppercase
    email_domain: str  # Extracted domain from email
    signup_date: datetime  # Parsed datetime object

# Sample raw records
raw_users = [
    {
        "name": "serkan yaşar",
        "email": "yasarserkan16@gmail.com",
        "signup_timestamp": "2024-05-08 09:20:00"
    },
    {
        "name": "serkan yasar",
        "email": "example@example.com",
        "signup_timestamp": "2024-04-12 14:45:30"
    }
]

# Transform function
def transform_user(user_data: UserInput) -> UserTransformed:
    name_upper = user_data.name.upper()  # Convert name to uppercase
    email_domain = user_data.email.split("@")[-1]  # Extract domain
    signup_date = datetime.strptime(user_data.signup_timestamp, "%Y-%m-%d %H:%M:%S")  # Convert string to datetime

    return UserTransformed(
        name_upper=name_upper,
        email_domain=email_domain,
        signup_date=signup_date
    )

# Process all users
transformed_users: List[UserTransformed] = []

for raw_user in raw_users:
    input_model = UserInput(**raw_user)  # Validate input
    transformed = transform_user(input_model)  # Transform
    transformed_users.append(transformed)

# Print results
for user in transformed_users:
    print(user)
