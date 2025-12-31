# CONTINUOUS INPUT
while True:
    inp = input(">").lower()
    if inp == "done": break

# DECORATIVE PRINT STATEMENTS USING F STRINGS
print(f"{"a":*^6}") # ^ means centre, so it aligns string a to the centre while putting * around it 

# TO GET ALL FUNCTIONS AND METHODS OF SOMETHING
dir(str)  # to get all functions and methods of a str
dir(int)  # to get all functions and methods of a int,etc

# TO GET ALL PUNCTUATIONS
from string import punctuation

# TO USE .TRANSLATE TO REPLACE OR REMOVE SOMETHING
s = "TestString" # Test String
s.translate(str.maketrans("","","")) # the first "" shows the old letter or the original, the second quotation shows the new letter or the one that will replace the original or old one , they can be left blank tho if nothing is to be replaced. 
# The last quotation is for removing things completely can be left blank if nothing is to be removed 


# To MERGE DICTIONARIES
X = {'A' : 'a','B' : 'b'}
Y = {'C' : 'c', 'D' : 'd'}
Z = {**X,**Y} #Merge X dict and Y dict together
# Note if two dictionaries keys are the same, it takes the key from right or the second dictionary  
print(Z)
