# Scrapping White House's Briefings and Statements Website
# Ref: https://www.whitehouse.gov/briefing-room/statements-releases/

# Goal: Extract all links that point to the briefings and statements
import requests
from bs4 import BeautifulSoup

webpage = requests.get(
    "https://www.whitehouse.gov/briefing-room/statements-releases/")
print("1. Website Response: ")
print(webpage.status_code)
print()

src = webpage.content
soup = BeautifulSoup(src)
links = soup.find_all("a")

print("2. Briefings: ")
for bs in links:
    if "Briefing" in bs.text:
        print(bs)
        print(bs.attrs['href'])

print()

print("3. Statements: ")
for bs in links:
    if "Statement" in bs.text:
        print(bs)
        print(bs.attrs['href'])

print()