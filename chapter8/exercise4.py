"""  Exercise 4: Find all unique words in a file 
Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used?
Would you download all his work, read it and track all unique words by hand?
Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.
 
Enter file: romeo.txt
 [Arise, But, It, Juliet, Who, already,
 and , breaks, east, envious, fair, grief,
 is, kill, light, moon, pale, sick , soft,
 sun , the, through, what, window,
 with, yonder]"""


from pathlib import Path
filePath = Path(r"C:\Users\HP\Documents\romeo.txt")
with open(filePath,mode="r",encoding="utf-8") as f:
    uniqueWords = list()
    for line in f:
        words = line.split()
        for word in words:
            if word not in uniqueWords:
                print("Adding word:", word)
                uniqueWords.append(word)
    
    uniqueWords.sort() # Lists is mutable , so it returns None, so here it's not passed into a variable
    print()
    print(f"Unique words in {filePath.name} sorted alphabetically")
    print(f"{"#":*^50}")
    for word in uniqueWords:
        print(word)