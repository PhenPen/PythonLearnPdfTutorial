""" Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average"""


nums = []
while True:
    inp = input(">")
    if inp.lower() == "done":
        break
    try :
        float(inp)
    except ValueError :
        print("Enter only numbers")
    else :
        num = float(inp)
        nums.append(num)

print(nums)
print(f"The largest number is {max(nums)} and the smallest number is {min(nums)}")
