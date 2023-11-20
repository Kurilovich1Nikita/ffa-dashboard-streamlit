import requests
import pandas as pd
from io import BytesIO
import os

# URL for the API endpoint
api_url = "https://www.rvo.nl/sites/default/files/2022-05/Varkensslachtingen.xlsx"

# Make a GET request to the API endpoint
response = requests.get(api_url)

if response.status_code == 200:
    # Create a BytesIO object from the content
    excel_data = BytesIO(response.content)

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_data, sheet_name='2022', header=0)  # Adjust sheet_name and header as needed

    # Create the 'API_data' directory if it doesn't exist
    directory = 'API_data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Example: Save the DataFrame to a CSV file in the 'API_data' directory
    csv_file = os.path.join(directory, "6varkensslachtingen.csv")
    df.to_csv(csv_file, index=False)

    print(f"API data retrieved and saved as {csv_file} successfully.")

else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")