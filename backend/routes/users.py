from fastapi import APIRouter
import boto3
import os

router = APIRouter()

# Spajanje na lokalni DynamoDB (endpoint iz Docker Compose)
dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv("AWS_REGION", "us-east-1"),
    endpoint_url=os.getenv("DYNAMODB_ENDPOINT", "http://localhost:8000")
)

users_table = dynamodb.Table('Users')  # Naziv tablice korisnika u DynamoDB

@router.get("/")
def get_users():
    response = users_table.scan()
    return response['Items']