""" Exercise 1: Download a copy of the file
 www.py4e.com/code3/words.txt
 Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary. """

from pathlib import Path
# filePath = Path(__file__).parent / "practice1.py"
filePath = Path(r"C:\Coding\Projects\VsCode\tutsPhen\pdfTuts\pythonLearnpdf\learningDocs\words.txt")

d = dict()

print(f"{'Words':*^78}") # decorative print statement
with open(filePath,mode="r",encoding="utf-8") as f:
    for line in f:
       words = line.strip().strip('/n').split()
       if words == [] : continue
       print(words)
       for word in words :
        if word != d :
           d[word] = word
       #for word in words:
        #    #d[word] = d.get(word,0) + 1
         #   d[word] = word

print()

print(f"{'Keys':*^78}")
print(d.keys())