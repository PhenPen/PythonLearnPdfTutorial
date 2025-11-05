""" Took Exercise 1 from Chapter 9 code and add counters to it, so it would print how many times each word appeared in the file words.txt """

from pathlib import Path
from string import punctuation #imported string.punctuation module to remove punctuation from words as seen in ln 17
# filePath = Path(__file__).parent / "practice1.py"
filePath = Path(r"C:\Coding\Projects\VsCode\tutsPhen\pdfTuts\pythonLearnpdf\learningDocs\words.txt")

d = dict()

# print(f"{'Words':*^78}") # Printing * heading was only meant for word spacing in original exercise
with open(filePath,mode="r",encoding="utf-8") as f:
    for line in f:
       words = line.strip().strip('/n').split()
       if words == [] : continue
       # print(words) # For outputting the words list per line
       for word in words :
              word = word.translate(str.maketrans('','',punctuation)) # To remove punctuation from words
              d[word] = d.get(word,0) + 1 #.get() gets the existing value, if empty it returns the default value, which has been set as 0 ,else it adds 1 to the existing value
        #if word != d :
           #d[word] = word

       #for word in words:
        #    #d[word] = d.get(word,0) + 1
         #   d[word] = word

#print() #Printing spaces was only meant for words and keys spacing in original exercise

print(f"{'Keys':*^78}")

lst = list(d.keys())
sortedLst = lst.sort()
for key in lst :
    print(f"{key} : {d[key]}")


