"""  Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.
 Enter a number: 4
 Enter a number: 5
 Enter a number: bad data
 Invalid input
 Enter a number: 7
 Enter a number: done
 16 3 5.333333333333333"""


nums = []
numTotal = 0
numCount = 0


while True:
    inputS = input(">")
    if inputS.lower() == "done" :
        break
    try :
        num = float(inputS)
    except ValueError :
        print("Invalid Input")
    else :
        nums.append(num)

for tNums in nums :
    numCount += 1
    numTotal += tNums

numAverage = numTotal / numCount

print(f"The total, count and average of {nums} is {numTotal}, {numCount} and {numAverage}")