import re

S = "The lazy fox jumps over the brown dog,The lazy fox jumps over the brown dog again"

print(re.search("the", S)) # Search for exactly the first occurrence the string "the" (case sensitive like capital)
print(re.match("the", S)) # Tries to match the first word of the string to the str it's looking for , which in this case # Returns None though as it doesn't match
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
# \s - space characters or white space characters (contains any thing that creates space eg " "(normal space), \t(tab space), \n(newline or line feed)), \r(carriage return), \f(form feed) and \v(vertical tab)
#\S - opposite of white space characters

# Note that \S also includes \w , as \S is anything that is not is not space 

#\d - digit characters (0-9)
#\D - opposite of digit characters or anything that is not a digit character 

#\b - word boundary ( used for matching words exactly) {and is used in the format \b<word>\b just like html tags eg \bcat\b matches cat but not catalog}
#\B - opposite of word boundary



# ALLCHARS IN REGEX NAMING

# When using re.match or re.search, instead of capturing a pattern and using match.group(0), match.group(1) etc to find the captured parts if there are multiple parts , we can name those parts

line = "Contact me at support@google.com"
email = re.search(r"([a-zA-Z0-9]+\S)*@(\S*[a-zA-Z])", line)
 # Without Naming , to retrieve the name and domain name for the email, we would have to do 

group1 = email.group(1) if email else None #Prints the name part
group2 = email.group(2) if email else None #Prints the domain part

# Note that the if email else None is used to avoid attribute errors in case there is no match found, if email will return True if there is a match else returns None

print(group1) # Name part  
print(group2) # Domain part

# Using all char naming
email = re.search(r"(?P<name>[a-zA-Z0-9]+\S)*@(?P<domain>\S*[a-zA-Z])", line)
# Adding the all chars ?P<name> for the name part and ?P<domain> for the domain part, we can use name and domain for email.group instead of numbers 

name_group = email.group('name') if email else None #Prints the name part
domain_group = email.group('domain') if email else None #Prints the domain part

# Note that the if email else None is used to avoid attribute errors in case there is no match found, if email will return True if there is a match else returns None

print(name_group) # Name part  
print(domain_group) # Domain part