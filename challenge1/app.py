from dotenv import load_dotenv
import os

load_dotenv()

AWS_KEY = os.getenv("AWS_KEY")
DB_URL = os.getenv("DB_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def connect_to_database():
    print("Connecting to production database...")

def call_aws_service():
    print("Calling AWS S3 service...")

if __name__ == "__main__":
    connect_to_database()
    call_aws_service()