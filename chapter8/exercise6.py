"""  Exercise 6:
 Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”.
 Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
"""

num = list()

while True:
    inp = input("Enter a number: ")
    if inp.lower() == "done": break
    try:   
        val = int(inp)
    except ValueError as e:
        print(f"Error thrown: {e}")
        print("Invalid input. Please enter a numeric value.")
    else:
        num.append(val)


maximum = max(num)
minimum = min(num)

print(f"All numbers entered are {num}")
print(f"The maximum number is {maximum} and the minimum number is {minimum}")
