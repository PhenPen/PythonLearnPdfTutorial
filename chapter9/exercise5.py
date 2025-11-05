"""  Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary. python school count.py
 Enter a file name: mbox-short.txt
 {media.berkeley.edu: 4, uct.ac.za: 6, umich.edu: 7,
 gmail.com: 1, caret.cam.ac.uk: 1, iupui.edu: 8}
"""

from pathlib import Path
filePath = Path(r"C:\Coding\Projects\VsCode\tutsPhen\pdfTuts\pythonLearnpdf\learningDocs\mbox-short.txt")

d = dict()

with open(filePath,"r",encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        # print(line) #  for debugging 
        if not line.startswith("From") : continue
        if line.startswith("From:") : continue
        line = line.split()
        emailWords = line[1]
        # print(emailWords) for debugging 
        emailWordsSplit = emailWords.split("@")
        # print(emailWordsSplit) for debugging
        domainName = emailWordsSplit[1]
        #print(domainName) for debugging
        

        d[domainName] = d.get(domainName, 0) + 1

print()
print(f"{"Domain Names and Values" :*^50}")
for k, v in d.items():
    print(f"{k} : {v}")
        #print(line) # for debugging
