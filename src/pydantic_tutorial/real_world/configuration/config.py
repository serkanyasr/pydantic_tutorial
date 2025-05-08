# configuration.py

import os
from pydantic import BaseModel, ValidationError, Field
from pydantic.class_validators import root_validator
from typing import Optional
import logging

# Setup logging configuration
logging.basicConfig(
    filename='configuration.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Config(BaseModel):
    app_name: str = Field(..., env='APP_NAME')  # APP_NAME env variable
    api_key: str = Field(..., env='API_KEY')  # API_KEY env variable
    debug: Optional[bool] = Field(False, env='DEBUG')
    db_url: str = Field(..., env='DB_URL')  # Database URL

    # Method to validate configuration after it's loaded
    @root_validator(pre=True)
    def check_configuration(cls, values):
        # Custom validation logic
        if not values.get('api_key'):
            raise ValueError("API key is required")
        return values

# Load configuration from environment variables
try:
    config = Config()
    logging.info("Configuration loaded successfully.")
except ValidationError as e:
    logging.error(f"Configuration validation failed: {e}")
    raise

# Display configuration
print(f"App Name: {config.app_name}")
print(f"Debug Mode: {config.debug}")
print(f"Database URL: {config.db_url}")
