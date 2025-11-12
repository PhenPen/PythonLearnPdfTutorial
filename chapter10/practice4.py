""" Converting Chapter 10, Exercise 3 to a function"""

def word_Frequency(filePath) : 
    from pathlib import Path

    d = dict()
    lst = list()


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