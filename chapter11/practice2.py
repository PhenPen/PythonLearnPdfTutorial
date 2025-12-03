import re

S = "The lazy fox jumps over the brown dog,The lazy fox jumps over the brown dog again"

print(re.search("the", S)) # Search for exactly the first occurrence the string "the" (case sensitive like capital)
print(re.match("the", S)) # Tries to match the first word of the string to the str it's looking for , which in this case # Returns None tho as it doesn't match
print(re.findall("the",S)) # Searches for all the occurrences, and returns them as strings
# print(re.finditer()) #Don't understand this yet # Should return a list of values or iterables ?
print(re.sub("the","#",S))

# . any character (can be placed anywhere)

# ANCHORS
# ^ beginning of string (placed at beginning of pattern)
# $ end of string (placed at end of pattern)

# CHARACTERS SETS AND NEGATION CHARACTER SETS
# [aeiou](Known as a character set , in this character set, we are checking for vowels as all the vowel including a,e,i,o,u)
# [^aeiou](Known as negation character set , in this character set, we are checking for all characters except vowels as all the vowels includes a,e,i,o,u)

#QUANTIFIERS
# * means 0 or more and is used to say check if this type of character exists, at least 0 or more times, to reduce the "more times"  we can add a question mark at the end eg *?
# + means 1 or more and is used to say check if this type of character exists, at least 0 or more times, to reduce the "more times"  we can add a question mark at the end eg +?
# {n} means n times and is used to say check if this character exists at least n times eg if n is 3, check for the string 3 times
# {n,} means n or more times and is used to say check if this character exists at least n times eg if n is 3, check for the string 3 times or more, to reduce the "more times"  we can add a question mark at the end eg {n,}?
# {n,m} means between n and m times , and is used to say check if this character exists between n and m times, eg if n is 3 and m is 5, check if it exists between 3 and 5 times 
# ? means either 0 or 1, check if the string exists 0 or 1 times 

# SHORTHAND CHARACTER ESCAPE SEQUENCES
# \w - word character (contains a-z,A-Z,0-9 and underscore(_))
# \W - opposite of word character
# \s - white space characters (contains any thing that creates space eg " "(normal space), \t(tab space), \n(newline or line feed)), \r(carriage return), \f(form feed) and \v(vertical tab)
#\S - opposite of white space characters

# Note that \S also includes \w , as \S is anything that is not is not space 

#\d - digit characters (0-9)
#\D - opposite of digit characters or anything that is not a digit character 

#\b - word boundary ( used for matching words exactly) {and is used in the format \b<word>\b just like html tags eg \bcat\b matches cat but not catalog}
#\B - opposite of word boundary


