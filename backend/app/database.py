import boto3

# Postavljanje konekcije na lokalni DynamoDB Docker container
dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://localhost:8000",  # Lokalni DynamoDB
    region_name="us-east-1",  # Mora se postaviti iako nije bitno lokalno
    aws_access_key_id="fakeMyKeyId",  # Bilo koji string (nije važno za lokalni Docker)
    aws_secret_access_key="fakeSecretAccessKey"
)

def create_table(table_name, key_schema, attribute_definitions):
    """Funkcija za kreiranje tablice u lokalnom DynamoDB, ako ne postoji."""
    existing_tables = [table.name for table in dynamodb.tables.all()]
    if table_name in existing_tables:
        print(f"Tablica {table_name} već postoji. Preskačem kreiranje.")
        return

    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5
            }
        )
        table.wait_until_exists()
        print(f"Tablica {table_name} uspješno kreirana!")
    except Exception as e:
        print(f"Greška pri kreiranju tablice {table_name}: {e}")

# Definicije tablica
tables = [
    {
        "name": "Users",
        "key_schema": [{"AttributeName": "user_id", "KeyType": "HASH"}],
        "attribute_definitions": [{"AttributeName": "user_id", "AttributeType": "S"}],
    },
    {
        "name": "Exhibitions",
        "key_schema": [{"AttributeName": "exhibition_id", "KeyType": "HASH"}],
        "attribute_definitions": [{"AttributeName": "exhibition_id", "AttributeType": "S"}],
    },
    {
        "name": "Artworks",
        "key_schema": [
            {"AttributeName": "artwork_id", "KeyType": "HASH"},
            {"AttributeName": "exhibition_id", "KeyType": "RANGE"}
        ],
        "attribute_definitions": [
            {"AttributeName": "artwork_id", "AttributeType": "S"},
            {"AttributeName": "exhibition_id", "AttributeType": "S"}
        ],
    },
    {
        "name": "Comments",
        "key_schema": [
            {"AttributeName": "comment_id", "KeyType": "HASH"},
            {"AttributeName": "artwork_id", "KeyType": "RANGE"}
        ],
        "attribute_definitions": [
            {"AttributeName": "comment_id", "AttributeType": "S"},
            {"AttributeName": "artwork_id", "AttributeType": "S"}
        ],
    }
]

# Kreiranje tablica
for table in tables:
    create_table(
        table["name"],
        table["key_schema"],
        table["attribute_definitions"]
    )