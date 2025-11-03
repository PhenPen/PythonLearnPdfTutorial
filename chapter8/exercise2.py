from pathlib import Path

filePath = Path(r"C:\Users\HP\Documents\mbox-short.txt")

fHand = open(filePath,mode="r",encoding="utf-8")
count = 0
for line in fHand:
    words = line.split()
    # print(Debug:, words)
    if len(words) == 0 or  words[0] != "From" : continue
    print(words[2])

