from pathlib import Path
import re

filepath = Path(r"learningDocs\mbox-short.txt")

try:
    with open (filepath,mode = "r", encoding= "utf-8") as file:
        newRevisionNo = []
        for line in file:
            matches = re.findall(r"^New Revision:\s*([0-9]+)",line)
            if matches:
                newRevisionNo.extend(matches)
            
        numbers = [int(num) for num in newRevisionNo if newRevisionNo != []]
        #print(numbers)
        length = len(numbers)
        #print(length)
        total = sum(numbers)
        average = total/length

        print(f"Values are {length} in total with a sum of {total} and average of {average}")
except FileNotFoundError:
    print("file not found")