""" Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
You can use split(/) to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL."""

import socket
import re
import time
url_domain ="" # Empty Variable for capturing domain from Regex
all_data = b"" # Empty variable for capturing byte data from socket 
count = 0 # For total count of byte data received 


# For Url, Port and Domain of Url
while True:
    url = input("Enter Url (Type q to quit): ")
    
    # Check for exit command first
    if url.lower() == "q":
        exit()
    

    port = (input("Enter Port (Press Enter if you don't know the port): "))

    # Port Checking and Conversion
    if port != "":
        port = int(port)
    

    # Regex for Host/Domain from URL
    test = re.search(r"^http[s]?://([^/]+)",url)
    # print(test) # For Debugging Regex

    #Invalid Error Checking
    if test is None:
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
        count = len(data) + count
        #time.sleep(0.25) # In case I want complete receive of bytes but I think I will just observe the download speeds for now
        print(len(data),count)
        all_data += data
except socket.gaierror as e:
    print(f"Socket Error : {e}")
except socket.error as e:
    print(f"Socket Error : {e}")


print()
print()
print(all_data.decode())


# Add try and except for url error checking , Not valid error and maybe urlError for checking if the error returns something
# find how to extract host and domain from url