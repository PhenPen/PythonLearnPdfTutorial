""" Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document."""

import socket
import re
import time
url_domain ="" # Empty Variable for capturing domain from Regex
all_data = b"" # Empty variable for capturing byte data from socket 
count_byte = 0 # For total count of byte data received 
count_char = 0 # For total count of characters 


# For Url, Port and Domain of Url
while True:
    url = input("Enter Url (Type q to quit): ")
    if url.lower == "q":
        exit()
    port = input("Enter Port (Press Enter if you don't know the port): ")

    # Port Checking and Conversion
    if port != "":
        port = int(port)
    

    # Regex for Host/Domain from URL
    test = re.search(r"^http[s]?://([^/]+)",url)
    # print(test) # For Debugging Regex

    #Invalid Error and Program Exit Checking
    if test is None: # findall returns an empty list instead of None if nothing is found
        print("Not a valid url. Try again")
    else:
        break

# Getting Host/Domain from URL
url_domain = test.group(1)

# Checking for Port
if port == "" and url.startswith("https"):
    port = 443
elif port == "" and url.startswith("http"):
    port = 80
else:
    port = port


try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((url_domain,port))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode() #Made mistakes here with the HTTP,the\,and the /r/n/r/n. Also, no whitespace allowed
    sock.send(cmd)

    while True:
        data = sock.recv(512)
        if len(data) < 1 : break
        count_byte = len(data) + count_byte
        #time.sleep(0.25) # In case I want complete receive of bytes but I think I will just observe the download speeds for now
        print(len(data),count_byte)
        all_data += data
except socket.gaierror as e:
    print(f"Socket Error : {e}")
except socket.error as e:
    print(f"Socket Error : {e}")


print()
print()
decoded = all_data.decode()
for character in decoded.split():
    count_char += 1
print(count_char)

print(decoded[:2900]) # To print the first 3000 characters



