"""  Exercise3 : Write a program that reads a file and prints the letters in decreasing order of frequency.Your program should convert all the input to lowercase and only count the letters a-z.Your program should not count spaces,digits,punctuation,or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies."""


from pathlib import Path
from string import punctuation

d = dict()
lst = list()

filePath = Path(r"learningDocs/mbox-short.txt")

try: 
    with open(filePath,"r",encoding = "utf-8") as file:
        for line in file:
            line = line.strip()
            for letter in line:
                if not letter.isalpha() : continue
                # print(letter) #for debugging
                letter = letter.lower()

                
                d[letter] = d.get(letter,0) + 1
        # print(d) #For debugging

        for Letter,Count in d.items():
            lst.append((Count,Letter))
        
        lst.sort(reverse=True)
        # print(lst) #For debugging
        
        for Count,Letter in lst: print(Letter,Count)
                    
                
   # print(d) #For debugging
                
except FileNotFoundError:
    print("File does not exist")