"""Exercise 3: Encapsulate this code in a function named count, and generalize it
 so that it accepts the string and the letter as arguments.

 The code : 
word = 'banana'

count = 0

for letter in word:

	if letter == 'a':

	count = count + 1

print(count)
  """

def count(word : str, letter : str) -> int :
	string = word
	letterInWord = letter
	count = 0
	
	for selectedLetter in string:
		if selectedLetter == letterInWord:
			count+= 1
	return count
	
wordA = input("Enter a word : ")
letterA = input("Enter a letter : ")
	
print(count(wordA, letterA))
