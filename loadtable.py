
import json
import boto3

dynamodb= boto3.resource('dynamodb', region_name= 'us-east-1')

table= dynamodb.Table('Sneakers')

with open("sneakerdata.json") as json_file:
    Sneakers_list= json.load(json_file)
    for sneaker in Sneakers_list:
        brand= sneaker['brand']
        types= sneaker['types']

        print( "Adding Sneaker:", brand, types)

        table.put_item (Item= sneaker)
