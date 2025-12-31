from urllib import request
from urllib.error import URLError, HTTPError
import ssl # SSL Module
import re  # Regular Expressions Module


# To ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL link :")
try:
    with request.urlopen(url,context=ctx) as file:
        html = file.read()
        links = re.findall(b'href="(http[s]?://.*)"',html)
        for link in links:
            print(link.decode())
except URLError as e:
    print(f"Could not open URL;   ERROR : {e}")


