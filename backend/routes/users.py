from fastapi import APIRouter
import boto3

router = APIRouter()

# Kreiranje konekcije s DynamoDB
dynamodb = boto3.resource('dynamodb')
users_table = dynamodb.Table('Users')  # Naziv tablice korisnika u DynamoDB

@router.get("/")
def get_users():
    response = users_table.scan()
    return response['Items']