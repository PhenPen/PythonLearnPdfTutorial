from pathlib import Path
import re 

filePath = Path(r"learningDocs/mbox-short.txt")
try:
    with open(filePath,mode="r",encoding="utf-8") as file:
        for line in file:
            line= line.strip()
            # print(line) #For debugging
            email = re.findall(r"[a-zA-Z0-9]+\S*@\S*[a-zA-Z]",line) #Must use backslashes not forward slashes
            #if len(email) >0 : print(email)
            xNum = re.findall(r"^X-\S+: d+",line)
except FileNotFoundError:
    print("File doesn't exist")


text = "Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772"

#print(re.findall(r"Details:\s*.+rev=([0-9]+)",text))

text2 = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
#print(re.findall(r"^From\s.+@[a-zA-Z.]+\s(.{3})\s.+",text2))

help(re.search)