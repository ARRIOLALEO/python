import requests
from bs4 import BeautifulSoup as bs
user = input('gime the user')
url = 'https://github.com/'+user
response = requests.get(url)
soup = bs(response.content)
print(soup)
