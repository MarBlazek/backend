import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1", endpoint_url="http://localhost:8001")
table = dynamodb.Table("exhibits")