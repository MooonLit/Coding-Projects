import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_largest_Japanese_companies"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the first table
    table = soup.find('table')
    
    # Convert the table to a DataFrame
    df = pd.read_html(str(table))[0]
    
    # Display the DataFrame
    print(df)
else:
    print("Failed to retrieve the webpage")
