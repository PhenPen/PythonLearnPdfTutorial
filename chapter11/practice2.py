import re

S = "The lazy fox jumps over the brown dog,The lazy fox jumps over the brown dog again"

print(re.search("the", S)) # Search for exactly the first occurrence the string "the" (case sensitive like capital)
print(re.match("the", S)) # Tries to match the first word of the string to the str it's looking for , which in this case # Returns None tho as it doesn't match
print(re.findall("the",S)) # Searches for all the occurrences, and returns them as strings
# print(re.finditer()) #Don't understand this yet # Should return a list of values or iterables ?
print(re.sub("the","#.",S))
