import requests
import pandas as pd
import os

# List of endpoints
endpoints = [
    "TableInfos",
    "UntypedDataSet",
    "TypedDataSet",
    "DataProperties",
    "CategoryGroups",
    "Slachtdieren",
    "Perioden"
]

data = {}

# Fetch data from each endpoint and store it in a dictionary
for endpoint in endpoints:
    url = f"https://opendata.cbs.nl/ODataApi/OData/7123slac/{endpoint}" #this path can differ (replace it with the correct one)
    response = requests.get(url)
    if response.status_code == 200:
        data[endpoint] = response.json()
    else:
        print(f"Failed to fetch data from {endpoint}")

# Create the 'API_data' directory if it doesn't exist
directory = 'API_data'
if not os.path.exists(directory):
    os.makedirs(directory)

# Convert and save the data to CSV in the 'API_data' directory
for endpoint, endpoint_data in data.items():
    df = pd.DataFrame(endpoint_data['value'])
    csv_file = os.path.join(directory, f"3{endpoint}.csv")
    df.to_csv(csv_file, index=False)