""" Exercise 3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression using the or logical operator with a single if statement."""

from pathlib import Path

filePath = Path(r"C:\Users\HP\Documents\mbox-short.txt")

fHand = open(filePath,mode="r",encoding="utf-8")
count = 0
for line in fHand:
    words = line.split()
    # print(Debug:, words)

    #if len(words) <3 : continue
    #if words[0] != "From" : continue
    if len(words) <3 or words[0] != "From" : continue
    print(words[2])

fHand.close()