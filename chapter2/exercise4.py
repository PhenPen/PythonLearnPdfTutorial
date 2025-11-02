"""  Exercise 4: Assume that we execute the following assignment statements:
 width = 17
 height = 12.0
 For each of the following expressions, write the value of the expression and the
 type (of the value of the expression).
 1. width//2
 2. width/2.0
 3. height/3
 4. 1 + 2 * """


width = 17
height = 12.0

expression1 = width//2
expression2 = width/2.0
expression3 = height/3
expression4 = 1 + 2 * 5

type1 = type(expression1)
type2 = type(expression2)
type3 = type(expression3)
type4 = type(expression4)

print(f"The value of 1 is {expression1} with a type {type1} \nThe value of 2 is {expression2} with a type {type2} \nThe value of 3 is {expression3} with a type {type3} \nThe value of 4 is {expression4} with a type {type4} \n ")