import requests
import csv
import os
import re

weeks_sequence = ','.join(str(week) for week in range(1, 53))

url = "https://www.ec.europa.eu/agrifood/api/beef/prices"
params = {
    'memberStateCodes': 'NL',
    'years': '2020',
    'months': '1,2,3,4,6,7,8,9,10,11,12',
    'weeks': weeks_sequence,
    'beginDate': '01/01/2020',
    'endDate': '31/12/2020',
    'carcassCategories': 'heifers,cows'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Initialize a dictionary to organize data by category
    categorized_data = {}

    for item in data:
        category = item.get('category')

        if category:
            # Replacing invalid characters for file names
            file_category = re.sub(r'[^\w\s-]', '', category)  # Replace invalid characters with '-'

            if file_category not in categorized_data:
                categorized_data[file_category] = []

            categorized_data[file_category].append(item)

    # Create the 'API-meat' directory if it doesn't exist
    directory = 'API_data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write categorized data to a CSV file for each category in the 'API-meat' directory
    for category, items in categorized_data.items():
        csv_file = os.path.join(directory, f'2_2020_{category}_data.csv')
        csv_headers = items[0].keys()  # Assuming the first entry contains all keys

        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
            writer.writeheader()
            writer.writerows(items)
else:
    print("Failed to fetch data from the API")