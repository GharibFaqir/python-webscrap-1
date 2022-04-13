# Youtube Link:

# Ensure that you have both beautifulsoup and requests install
# >> pip install bs4
# >> pip install requests
import requests
from bs4 import BeautifulSoup

# Using the requests module, we use the "get" function
# web page goes as argument
result = requests.get("https://www.google.com/")

# If website is accessible
# than response = 200 OK
print("1. Webpage Response: ")
print(result.status_code)
print()
# Other HTTPS Status Codes:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Access header of webpage, to make sure
# we have accessed the correct website
print("2. HTTP Headers: ")
print(result.headers)
print()

# Accessing content on webpage
src = result.content
print("3. Webpage Content: ")
print(src)
print()

# Beautify raw data through soup
soup = BeautifulSoup(src)

# To get all the links from webpage
print("4. Print all links: ")
links = soup.find_all("a")
print(links)
print()

# Get specific link
print("5. Get link and href: ")
for x in links:
    if "About" in x.text:
        print(x)
        print(x.attrs['href'])

print()

#