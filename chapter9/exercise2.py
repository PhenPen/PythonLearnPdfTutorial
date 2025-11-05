""" Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From" then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
 Sample Line:
 From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

 Sample Execution:
 python dow.py
 Enter a file name: mbox-short.txt
{Fri: 20, Thu: 6, Sat: 1} """


from pathlib import Path
filePath = Path(r"C:\Coding\Projects\VsCode\tutsPhen\pdfTuts\pythonLearnpdf\learningDocs\mbox-short.txt")

dEmail = dict()

try:
    with open(filePath,mode="r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("From:"):continue
            if line.startswith("From"):
                # print(line)  #For debugging
                words = line.split()
                day = words[2]
                # print(day)
                dEmail[day] = dEmail.get(day,0) + 1
                
                #print(dEmail)
                
                

        

                
        print(dEmail)

            # print(line) # For debugging 
except :
    print("File cannot be opened:",filePath)

