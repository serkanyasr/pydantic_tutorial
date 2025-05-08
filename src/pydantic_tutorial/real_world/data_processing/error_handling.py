import logging
from pydantic import BaseModel, ValidationError, EmailStr, conint
from typing import List, Tuple
import json

# Setup logging configuration
logging.basicConfig(
    filename='app.log',  # Log dosyasına yazacağız
    level=logging.DEBUG,  # DEBUG seviyesindeki logları alacağız
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Customer(BaseModel):
    name: str
    age: conint(gt=0) # type: ignore
    email: EmailStr

# Simulated raw data
raw_customers = [
    {"name": "Ali", "age": 28, "email": "ali@example.com"},
    {"name": "Zeynep", "age": -3, "email": "zeynep@example.com"},  # Invalid age
    {"name": "Ahmet", "age": 35, "email": "ahmet[at]example.com"},  # Invalid email
    {"name": "Mehmet", "age": 40, "email": "mehmet@example.com"},
]

valid_customers: List[Customer] = []
errors: List[Tuple[int, str]] = []  # To keep index + error message
error_log = []  # For saving errors to a separate file

# Process records
for index, record in enumerate(raw_customers):
    try:
        customer = Customer(**record)  # Validate data
        valid_customers.append(customer)
        logging.info(f"Record {index} processed successfully: {record}")  # Log success
    except ValidationError as e:
        error_message = f"[Error in record {index}] {e}"  # Format error message
        logging.error(error_message)  # Log error
        errors.append((index, str(e)))  # Store error
        error_log.append({"index": index, "error": str(e), "data": record})  # Log to separate list

# Output results
print("\n--- VALID CUSTOMERS ---")
for cust in valid_customers:
    print(cust)

print("\n--- ERRORS ---")
for i, msg in errors:
    print(f"Record {i} failed:\n{msg}")

# Save errors to a file
with open("error_records.json", "w") as f:
    json.dump(error_log, f, indent=4)

print("\nError details have been saved to 'error_records.json'")
