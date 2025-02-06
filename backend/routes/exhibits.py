from fastapi import APIRouter
import boto3

router = APIRouter()

# Kreiranje konekcije s DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Exhibits')  # Naziv tvoje tablice u DynamoDB

@router.get("/")
def get_exhibits():
    response = table.scan()
    return response['Items']

@router.post("/")
def create_exhibit(exhibit: dict):
    response = table.put_item(Item=exhibit)
    return {"message": "Exhibit added successfully", "exhibit": exhibit}