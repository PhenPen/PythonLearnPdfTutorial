""" Sockets Part I"""
import socket


#Address is the location of what you are requesting too or from eg an Internet IpV4 address, a bluetooth device
#Sock_ refers to the type of communication socket used eg TCP(Communication is sent in continuous streams eg like a football match stream), UDP (communication is sent in packets)
#host and domain name often refers to the second part in a website after the protocol eg in a website https://api.dat.org  , https is the protocol,api the host name and dat.org the domain name, in some websites tho, it could be https://data.org  , the data.org is both the domain name and host name
#Port can be described as the door to the server of the domain name, of where I have to pass through if I want to communicate with that server 

addressFamily = socket.AF_INET #AF_INET means addressFamily for INTERNET IPV4
communicationSock_ = socket.SOCK_STREAM #SOCK_STREAM is another name for TCP 

host_domainName ="data.pr4e.org"
port :int = 80


mySock = socket.socket(addressFamily,communicationSock_) 
mySock.connect((host_domainName,port)) # It takes 2 positional arguments in a tuple based on the address, for IPV6, it takes 4 arguments in a tuple. it's always in a tuple so connect can receive only one input regardless of how many arguments the input takes in 

CMD : bytes = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # This means using command GET to get data on this absolute address path with the HTTP protocol 1.0 , then escape sequences carriage return \r(Which carries the cursor to beginning of line) and newline \n which is used to create new lines. Note that the escape sequences are done twice, .encode() converted the data to bytes ,which is usually in utf-8 encoding
# I could have also done b'GET ....' instead of encode(), it will give bytes all the same

mySock.send(CMD)

while True:
    data :bytes = mySock.recv(512)
    if len(data) < 1 :
        break
    print(data.decode(),end=" ")

    