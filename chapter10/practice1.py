tu = (1,2,3,)

t = () # empty tuple
t =tuple() # empty tuple using constructor

t = (1,) # single element tuple

print(type(t))

# Tuple are immutable and hashable
# t[0] = 10 # TypeError: 'tuple' object does not support item assignment # It also means tuple can be used as key in dictionary or element in set

tup = ("tuple",)
print(tup) # The comma here makes it behave like a single item, in the tuple. To iterate directly over it, we could call the type tuple on it (Check ln 16:ln 18)

print()
tupAD = tuple("tuple")
print(tupAD)

# You can print out part of the tuple by indexing eg tupAD[0] , we can also print out parts of the tuple by slicing eg tupAD [0:2] 

# You can't remove or add items to a tuple but you can replace an item with slicing
# tupAD = ("A",) + t[1:] #Creates a new tuple based on A as the first character and the remainder of the former tupAD tuple

txt = "but soft what light in yonder window breaks"
words = txt.split()
ti = list()


#unpacking of tuples in python # This also works for lists

addr = "chiben@gmail.com"
addrName,addrDomain = addr.split("@") #since split divides the email into 2, the first part goes to the first variable, and the second part , to the second variable

print(addrDomain) #prints the second part in the second variable

#To sort out dicts, we have to convert it to a list, then sort it 

d = {"b":1, "a":10, "c":22}
lst = list(d.items())
# print(lst)
lst.sort() #lst.sort() returns None as it is not a string so we do not assign it to lst again
print(lst)


lambda x : x + 1
