""" Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives   and all), not lines."""

import socket
import re
import time
url_domain ="" # Empty Variable for capturing domain from Regex
all_data = b"" # Empty variable for capturing byte data from socket 
count = 0 # For total count of byte data received 


# For Url, Port and Domain of Url
while True:
    url = input("Enter Url (Type q to quit): ")
    port = (input("Enter Port (Press Enter if you don't know the port): "))

    # Port Checking and Conversion
    if port != "":
        port = int(port)
    

    # Regex for Host/Domain from URL
    test = re.findall(r"^http[s]?://([^/]+)",url)
    # print(test) # For Debugging Regex

    #Invalid Error and Program Exit Checking
    if test == []: # findall returns an empty list instead of None if nothing is found
        print("Not a valid url. Try again")
    elif url.lower == "q":
        exit()
    else:
        break

# Getting Host/Domain from URL
for te in test: # Regex Match and Search was having issues extracting group so I used findall and a for loop
    url_domain = te

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
#print(all_data.decode())
pos = all_data.find(b"\r\n\r\n")
print(all_data[pos+4:].decode())

# Add try and except for url error checking , Not valid error and maybe urlError for checking if the error returns something
# find how to extract host and domain from url