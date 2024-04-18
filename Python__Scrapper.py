import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the Excel file containing the URLs
df = pd.read_excel(r" ") # input file path

# Initialize a list to store the extracted data
data_list = []

# Iterate over each URL in the DataFrame
for index, row in df.iterrows():
    url = row.iloc[0]  # Assuming the URLs are in the first column of the Excel file

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the title and meta description
        title = soup.title.text if soup.title else "No title found"
        meta_description = soup.find("meta", attrs={"name": "description"})["content"] if soup.find("meta", attrs={
            "name": "description"}) else "No meta description found"

        # Create a dictionary containing the extracted information
        data = {
            "url": url,
            "title": title,
            "meta_description": meta_description
        }

        # Append the dictionary to the data list
        data_list.append(data)

    except Exception as e:
        print(f"Error processing URL: {url}, {e}")

# Convert the data list to a pandas DataFrame
result_df = pd.DataFrame(data_list)

# Save the DataFrame to a CSV file
result_df.to_csv(r" ", index=False) # output file path

# Print the DataFrame
print(result_df)
