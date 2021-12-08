
import boto3

def create_sneaker_table(dynamodb=None):
     if not dynamodb:
         dynamodb = boto3.resource('dynamodb', region_name= 'us-east-1')

     table = dynamodb.create_table(
         TableName='Sneakers',
         KeySchema=[
             {
                 'AttributeName': 'brand',
                 'KeyType': 'HASH'  # Partition key
             },
             {
                 'AttributeName': 'types',
                 'KeyType': 'RANGE'  # Sort key
             }
         ],
         AttributeDefinitions=[
             {
                 'AttributeName': 'brand',
                 'AttributeType': 'S'
             },
             {
                 'AttributeName': 'types',
                 'AttributeType': 'S'
             },

         ],
         ProvisionedThroughput={
             'ReadCapacityUnits': 10,
             'WriteCapacityUnits': 10
         }
     )
     return table

if __name__ == '__main__':
     sneaker_table = create_sneaker_table()
     print("Table status:", sneaker_table.table_status)
