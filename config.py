from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
aws_access_key_id = os.getenv("AWS_SERVER_PUBLIC_KEY")
aws_secret_access_key = os.getenv("AWS_SERVER_SECRET_KEY")

# S3 bucket and JSON file paths
s3_bucket = "real-estate-data-lake-2024"  
json_file_key = "real_estate_data.json"  