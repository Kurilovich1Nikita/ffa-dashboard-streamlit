import requests
import pandas as pd
import os

# URL for the API endpoint
api_url = "https://www.rvo.nl/sites/default/files/2022-05/Prijzen-vleeskalveren.xlsx"

# Make a GET request to the API endpoint
response = requests.get(api_url)

if response.status_code == 200:
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(response.content)

    # Create the 'API-data' directory if it doesn't exist
    directory = 'API_data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Example: Save the DataFrame to a CSV file in the 'API-data' directory
    csv_file = os.path.join(directory, "4Prijzen-vleeskalveren.csv")
    df.to_csv(csv_file, index=False)

    print(f"API data retrieved and saved as {csv_file} successfully.")

else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")
