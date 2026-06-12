import requests
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

header_row = soup.find("tr")

print("Product Rows:")

for product in header_row.next_siblings:
    print(product.text)

print("Price associated with image:")

extract_images = soup.find_all("img")

for image in extract_images:
    extract_price = image.parent.previous_sibling
    print(image)
    print(extract_price.text)

