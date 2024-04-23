import os
import requests
import csv
import re

# Specify file location
file_name = "given_names.csv"
file_location = os.path.join(os.getcwd(), file_name)

# API URL and initial parameters
api_url = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "list": "categorymembers",
    "cmnamespace": 0,
    "cmlimit": 500,
    "cmtitle": "Category:Given_names",
    "format": "json"
}

# Function to fetch category members
def fetch_category_members(url, params):
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Function to clean title
def clean_title(title):
    title = re.sub(r'\s*\(.*?\)\s*', '', title)  # Remove text within parentheses and surrounding whitespace
    return title.strip()  # Remove leading and trailing whitespace

# Main function to iterate through pages and save titles to CSV
def main():
    try:
        with open(file_location, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            while True:
                data = fetch_category_members(api_url, params)
                category_members = data['query']['categorymembers']
                for member in category_members:
                    title = clean_title(member['title'])
                    writer.writerow({'Title': title})
                
                if 'continue' in data:
                    params.update(data['continue'])
                else:
                    break
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
