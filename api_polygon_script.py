import json
import requests
import pandas as pd
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

# API key
API_KEY = os.environ.get('POLYGON_API_KEY') # This is best practice

# Set up MongoDB connection user credentials
MONGO_DB_USER = os.environ.get('MONGO_DB_USER')
MONGO_DB_PASSWORD = os.environ.get('MONGO_DB_PASSWORD')
MONGO_CONNECTION_STRING = f'mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@pythonapidemo.bbuekoq.mongodb.net/'

# Set up MongoDB connection
client = pymongo.MongoClient(MONGO_CONNECTION_STRING, tls=True, tlsAllowInvalidCertificates=True)

# Create a database
db = client['pythonapidemo']

# Polygon API URL
API_URL__META = f'https://api.polygon.io/v2/aggs/ticker/META/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&apiKey={API_KEY}'
API_URL__TESLA = f'https://api.polygon.io/v2/aggs/ticker/TSLA/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&apiKey={API_KEY}'
lookup_list = [API_URL__META, API_URL__TESLA]

print('Printing lookup list:...')
print(lookup_list)
# print('Printing API URL:...')
# print(API_URL)

# Create a function in order to make API requests based on URL that we pass in.
def make_request(url):
    import pandas as pd

    try:
        json_data = requests.get(url)
        print('Printing response...')
        print(json_data)

        # Convert JSON into pandas dataframe
        json_results = json_data.json()['results']
        ticker = json_data.json()['ticker']
        
        return json_results, ticker
    except:
        print('An error occurred')
        return {}

# For every api url in the lookup list, make a request and print the response.
for api_url in lookup_list:

    json_results, ticker = make_request(api_url)
    print('Printing ticker...')
    print(ticker)

    # Make collection with ticker name from response.
    collection = db[ticker]
    print(client)
    print(collection)

    # Insert a json data from results into the collection
    print('Writing json results to MongoDB, please wait...')
    collection.insert_many(json_results)

