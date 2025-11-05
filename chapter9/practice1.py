""" Chapter 9: Practice 1 - Working with Dictionaries in Python"""

d = dict()  # Create an empty dictionary method 1 (type method)
e = {}    # Create an empty dictionary method 2 (Curly braces method)

d['name'] = 'John' #adding key-value pairs to a dict method 1
print(d)
print()

d = {'name': 'James', 'age': '30', 'city': 'New York'} #adding key-value pairs to a dict method 2    

# Note the dictionary in ln 10 overwrites the dictionary in ln 6 as it comes before it and both use the same variable name 'd'

print(d)

print(d['age']) #accessing value by key

print('age' in d) #checking if a key exists in a dict, returns True if it exists, else False

print(30 in list(d.values())) #checking if a value exists in a dict, returns True if it exists, else False

print()
print()
print()



