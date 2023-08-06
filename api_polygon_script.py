import json
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# API key
API_KEY = os.environ.get('POLYGON_API_KEY') # Not best practice, Passwords shuold be kept safe.

# Polygon API URL
API_URL = f'https://api.polygon.io/v2/aggs/ticker/META/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&apiKey={API_KEY}'
print('Printing API URL:...')
print(API_URL)

# Make API request
response = requests.get(API_URL)
# print('Printing response...')
# print(response.text)

# Convert to JSON object
json_data = json.loads(response.text)
# print('Printing JSON data...')
# print(json_data)

# Convert JSON into pandas dataframe
df = pd.DataFrame(json_data['results'])
print(df.head())

# save the dataframe to csv
df.to_csv('polygon_data.csv')