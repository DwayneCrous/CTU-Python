import requests
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

header_row = soup.find("tr")

# Printing all of the product rows
print("Product Rows:")

for product in header_row.next_siblings:
    print(product.text)

# Printing all prices associated with the images
print("Price associated with image:")

extract_images = soup.find_all("img")

for image in extract_images:
    extract_price = image.parent.previous_sibling
    print(image)
    print(extract_price.text)

# Printing all the children of the gift list element
print("All children of giftList element")

gift_list_element = soup.find_all(id="giftList")

for children in gift_list_element:
    children.children
    print(children.text)

#.children gets is direct children only and returns a list
#.decendants gets all of the nested children recursively