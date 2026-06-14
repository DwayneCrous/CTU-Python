import requests
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

one_attribute_tags = soup.find_all(lambda tag: len(tag.attrs) == 1)

print("Tags with one attribute:")
for tag in one_attribute_tags:
    print(f"{tag.name}")

t_tags = soup.find_all(lambda tag: tag.name.startswith('t'))

print("\nTags starting with the letter t:")
for tag in t_tags:
    print(f"{tag.name}")