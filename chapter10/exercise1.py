"""  Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
 After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
 Sample Line:
 From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
 Enter a file name: mbox-short.txt
 cwen@iupui.edu 5
 Enter a filename: mbox.txt
 zqian@umich.edu 195"""

from pathlib import Path

filePath = Path(r"learningDocs/mbox-short.txt")
d = dict()
lst = list()

try:
    with open(filePath,"r",encoding = "utf-8") as file:
        for line in file:
            line = line.strip()
            if not line.startswith("From") : continue
            if line.startswith("From:") : continue
            # print(line) #For debugging
            line = line.split()
            addr = line[1]

            d[addr] = d.get(addr,0) + 1
        # print(d) #For debugging
        for email,count in d.items():
            lst.append((count,email))
        lst.sort(reverse=True)
        maxCount,Email = lst[0]
        print(Email,maxCount)
except FileNotFoundError:
    print("File not found")