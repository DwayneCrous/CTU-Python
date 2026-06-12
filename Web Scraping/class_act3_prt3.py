import requests
import re
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

pattern = re.compile(r'\.\./img/gifts/img.*\.jpg')

images = []
for img in soup.find_all("img", src=pattern):
    images.append(img['src'])

print(images)