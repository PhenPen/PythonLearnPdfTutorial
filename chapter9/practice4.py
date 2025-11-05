""" Modified code from chapter 9 exercise 2 to give the email in dict values instead of only counting it  """

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
                
                if day not in dEmail:
                    dEmail[day] = []
    
                
                dEmail[day].append(line)

        

                
        for keys,values in dEmail.items():
            print(f"{keys} : {values} ")

            # print(line) # For debugging 
except :
    print("File cannot be opened:",filePath)

