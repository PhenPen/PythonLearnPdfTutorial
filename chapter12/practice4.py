""" Using urlib instead of sockets"""

import urllib.request

d = {}
words = []

with urllib.request.urlopen('http://data.pr4e.org/romeo.txt') as urlFile:
    for line in urlFile:
        #print(line.decode().strip())  # Decode bytes to string and strip newline
        # Note that this doesn't give headers like the sockets but only the body data
        words.extend(line.decode().strip().split())
        for word in words:
            d[word] = d.get(word,0) + 1

    #print(d) #For dict debugging

# Writing words to file
with open(r"chapter12/text.txt","w",encoding= "utf-8") as file:
    file.write("Word Count from urlib based on practice 4 \n")
    file.write("Word : Count \n")
    for word,count in d.items():
        file.write(f"{word} : {count}\n" )
        print(f'{word} added with count {count}')
