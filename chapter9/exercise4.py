"""  Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.
 Enter a file name: mbox-short.txt
 cwen@iupui.edu 5
 Enter a file name: mbox.txt
 zqian@umich.edu 195"""

# Took code from chapter 9 exercise 3
from pathlib import Path
filePath = Path(r"C:\Coding\Projects\VsCode\tutsPhen\pdfTuts\pythonLearnpdf\learningDocs\mbox-short.txt")

dEmail = dict()
try:
    with open(filePath,mode= "r",encoding="utf-8") as file:
        for line in file:
            line.strip()
            if line.startswith("From"):
                words = line.split()
                email = words[1]
                #print(email)

               
                dEmail[email]=dEmail.get(email,0) + 1
                #print(dEmail)

    #print(dEmail)
    maxiNum = max(list(dEmail.values()))
    keyEmail = [k for k,v in dEmail.items() if v == maxiNum]
    for email in keyEmail: print(f"{email} : {maxiNum} emails")
except:
    pass