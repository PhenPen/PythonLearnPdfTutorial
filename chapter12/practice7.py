from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# Creating an ssl object 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL : str = input("Enter URL : ")
with urlopen(URL, context=ctx) as file:
    html = file.read()

soup = BeautifulSoup(html,"html.parser")
anchorTags = soup('a')
for tag in anchorTags:
    print(tag.get('href',None))
