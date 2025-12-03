""" Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several small web pages as well as some larger web pages."""

from bs4 import BeautifulSoup
from urllib import request, error
import ssl

# SSL Object creation
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL :")

try:
    with request.urlopen(url,context=ctx) as file :
        html = file.read()
except error.HTTPError as e :
    print(f"Error with HTTP file : {e}")
    html = ""
except error.URLError as e :
    print(f"Error with URL : {e}")
    html = ""

if html != "" :
    soup = BeautifulSoup(html,'html.parser')
    length = len(soup('p')) # Counting the number of paragraph tags in the HTML document

    print(f"Number of Paragraph tags : {length}")
