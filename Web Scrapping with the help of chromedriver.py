from selenium import webdriver
import docx
import pandas as pd

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Function to scrape data from a URL
def scrape_data(url):
    driver.get(url)
    # Scraping logic here
    # Example: Extracting title and returning it
    title = driver.title
    return title

# Read the Word document
doc = docx.Document(r"C:\Users\Dell\PycharmProjects\pythonProject4\Python Assigment 2.docx")

# List to store scraped data
scraped_data = []

# Loop through each paragraph in the document
for paragraph in doc.paragraphs:
    url = paragraph.text.strip()  # Assuming each paragraph contains a URL
    if url.startswith("http"):
        title = scrape_data(url)
        scraped_data.append({"URL": url, "Title": title})

# Close the webdriver
driver.quit()

# Create a DataFrame from the scraped data
df = pd.DataFrame(scraped_data)

# Save DataFrame to Excel
df.to_excel("scraped_data.xlsx", index=False)
