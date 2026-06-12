import requests
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/warandpeace.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

green_spans = soup.findAll("span", class_="green")

for span in green_spans:
    print(span.text)