"""  Exercise 2: Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file."""

from pathlib import Path

filePath = Path(r"C:\Users\HP\Documents\mbox-short.txt")

fHand = open(filePath,mode="r",encoding="utf-8")
count = 0
for line in fHand:
    words = line.split()
    # print(Debug:, words)
    #if len(words) <0 : continue
    if len(words) <3 : continue
    if words[0] != "From" : continue
    print(words[2])

fHand.close()

# Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

# The line not properly guarded is the print(words[2]), in some cases, the line might be more than 0 but less not up to 2, hence index error could occur again if that type of line occurs eg From Stephen , For the above example, there is no index[2], hence an error could occur

#Ln 12 was modified to add another if condition to check if len(words) < 3 , then continue to next line as seen in ln 13
