import requests
from bs4 import BeautifulSoup

url = "https://www.nasdaq.com/market-activity/stocks/screener"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

download_link = soup.find("a", class_=".ns-download-1")

if download_link:
    csv_url = download_link["href"]

    csv_response = requests.get(csv_url)

    with open("nasdaq_data.csv", "wb") as csv_file:
        csv_file.write(csv_response.content)
    print("CSV file downloaded successfully.")
else:
    print("Download link not found.")
