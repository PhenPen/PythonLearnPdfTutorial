"""  Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents."""

from urllib import request
import ssl
from urllib.error import HTTPError, URLError

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = b""
word_count = 0
try:
    with request.urlopen("http://data.pr4e.org/romeo.txt", context=ctx) as file :
        data = file.read()
except HTTPError as e:
    print(f"HTTP Error : {e} ")
except URLError as e:
    print(f"Error with URL : {e} ")


# print(data.decode())

# WORD COUNT
for word in data.decode():
    word_count += 1

if word_count == 0:
    print("No words received, Word count = 0")
else:
    print(f"Word count : {word_count}")

# To print only the first 3000 characters
print(data.decode()[:2900])
