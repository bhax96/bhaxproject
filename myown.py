#import libraries
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# specify the url
content="https://en.wikipedia.org/wiki/Sachin_Tendulkar"

page = urlopen(content)                                                                          
                                                       
                                                                           
                                                                          
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
content = soup.find('div', {"class": "mw-parser-output"})

article = ''
for i in content.findAll('p'):
    article = article + ' ' +  i.text
print(article)

b = bytes(article, 'utf-8')

# Saving the scraped text
with open('sachin1.text', 'wb') as file:
    b.decode()
    file.write(b)
