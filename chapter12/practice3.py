""" Sockets Part III"""

import socket, time

mySock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org',80))
CMD = 'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode()
mySock.sendall(CMD)

count :int = 0
pictureB : bytes = b''
while True:
    data = mySock.recv(5120)
    if len(data) < 1: break
    time.sleep(0.25) #Used to slow the requests (the .recv() buffer requests) so that the server has more time to fill up the data received

    #without the sleep module, the server sends data with ever request, eg len(data) has a max of 5120 but sometimes it doesn't reaches it fully, with add sleep, most times it reaches the max data that can be sent. The amount of time.sleep also matters, if the time is too much(like 5 sec), the program could seem slow, and too small, not enough time for the server to catch up

    count += len(data) #To find the total of the bytes received
    print(len(data),count) #Prints the immediate data length received and the total count of data so far
    pictureB += data #Appends all bytes received to the pictureB variable
mySock.close()

#Checking for end of header
pos = pictureB.find(b"\r\n\r\n")
print("Header length",pos)
print(pictureB[:pos].decode())

#Checking for body
picture = pictureB[pos+4:] #added +4 to the index, because of the \r\n\r\n takes 4 bytes , so adding 4 gives index of the body

#Writing binary to file
with open("chapter12/stuff.jpg",mode = "wb") as f:
    f.write(picture)