# Scrapping White House's Briefings and Statements Website
# Ref: https://www.whitehouse.gov/briefing-room/statements-releases/

# Goal: Extract all links that point to the briefings and statements
import requests
from bs4 import BeautifulSoup

webpage = requests.get(
    "https://www.whitehouse.gov/briefing-room/statements-releases/")

src = webpage.content
soup = BeautifulSoup(src)

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    if a_tag == None:
        urls.append("Empty")
        continue
    urls.append(a_tag.attrs['href'])

print(urls)