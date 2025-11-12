""" Modified Exercise 5 from ln 16 to ln 20"""
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
        emailWords_Name , emailWords_Domain = emailWords.split("@") #Changed ln 16 and 18 to make it shorter
        # print(emailWordsSplit) for debugging
        # domainName = emailWordsSplit[1] #Former line used , changed to make everything shorter
        #print(emailWords_Domain) for debugging
        

        d[emailWords_Domain] = d.get(emailWords_Domain, 0) + 1

print()
print(f"{"Domain Names and Values" :*^50}")
for k, v in d.items():
    print(f"{k} : {v}")
        #print(line) # for debugging
