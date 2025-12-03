""" Exercise 2: Write a program to look for lines of the form:
 New Revision: 39772
 Extract the number from each of the lines using a regular expression
 and the findall() method. Compute the average of the numbers and
 print out the average as an integer.
 Enter file:mbox.txt
 38549
 Enter file:mbox-short.txt
 39756
"""

from pathlib import Path
import re

filepath = Path(r"learningDocs\mbox-short.txt")

try:
    with open (filepath,mode = "r", encoding= "utf-8") as file:
        newRevisionNo = []
        for line in file:
            matches = re.findall(r"^New Revision:\s*([0-9]+)",line) #used r string to avoid escape characters issues 
            if matches:
                newRevisionNo.extend(matches)
            
        numbers = [int(num) for num in newRevisionNo if newRevisionNo != []]
        #print(numbers) #For debugging
        length = len(numbers)
        #print(length) #For debugging 
        total = sum(numbers)
        average = total/length
        

        print(f"Values are {length} in total with a sum of {total} and average of {average}")
except FileNotFoundError:
    print("file not found")