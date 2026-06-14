import requests
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"
response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

image_source = [img.get('src') for img in soup.find_all('img')]

print(image_source)

#extract all <a> tags and store their attributes

a_tags = [a.get('href') for a in soup.find_all('a')]
print(a_tags)