""" Exercise 1: Write a while loop that starts at the last character in the string and
 works its way backwards to the first character in the string, printing each letter on
 a separate line, except backwards."""


string = "Character"
length = len(string)
lengthCount = length - 1

while lengthCount >= 0:
    print (f"{string[lengthCount]} ")
    lengthCount -= 1 






