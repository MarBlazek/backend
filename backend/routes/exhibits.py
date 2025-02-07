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

table = dynamodb.Table('Exhibits')  # Naziv tvoje tablice u DynamoDB

@router.get("/")
def get_exhibits():
    response = table.scan()
    return response['Items']

@router.post("/")
def create_exhibit(exhibit: dict):
    response = table.put_item(Item=exhibit)
    return {"message": "Exhibit added successfully", "exhibit": exhibit}