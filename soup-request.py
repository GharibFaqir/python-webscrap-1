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
print(result.status_code)

# Other HTTPS Status Codes:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Access header of webpage, to make sure
# we have accessed the correct website
print(result.headers)