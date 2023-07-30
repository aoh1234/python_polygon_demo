import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API key
API_KEY = 'PGY2hHN4ls4x_sN3uk0FhIluBcMsLuJT'

# Polygon API URL
API_URL = f'https://api.polygon.io/v2/aggs/ticker/META/range/1/day/2023-01-01/2023-07-20?adjusted=true&sort=asc&apiKey={API_KEY}'
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

# mean statistics
print('Printing mean statistics...')
print(df.describe())

# visualize data using matplotlib
plt.plot(df['c'], color='green')
plt.plot(df['h'], color='black')
plt.plot(df['l'], color='red')
plt.title('Polygon.io Stock Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()
