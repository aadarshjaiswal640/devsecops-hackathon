AWS_KEY = "AKIAIOSFODNN7EXAMPLE123"
DB_URL = "postgresql://admin:SuperSecret99@localhost/prod"
SECRET_KEY = "super-secret-key"
DB_PASSWORD = "Password123!"

def connect_to_database():
    print("Connecting to production database...")

def call_aws_service():
    print("Calling AWS S3 service...")

if __name__ == "__main__":
    connect_to_database()
    call_aws_service()