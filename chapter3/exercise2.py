""" Exercise 2: Rewrite your pay program using try and except so that your pro
gram handles non-numeric input gracefully by printing a message and exiting the
 program. The following shows two executions of the program:

 Enter Hours: 20
 Enter Rate: nine
 Error, please enter numeric input
 Enter Hours: forty
 Error, please enter numeric input """


# this is like a copy of my last program (index 3.1)
# Changed line 19 and 27 from program 3.1, to match instructions


# Former pay computation index = 2.3
while True :
    try :
        ratePerHour = float(input("Enter rate per hour :"))
    except ValueError :
        print("\n Error, please enter numeric input")
    else :
        break

while True :
    try:
        hours = float(input("Enter number of hours : "))
    except ValueError:
        print("\n Error, please enter numeric input ")
    else :
        break


if hours > 40 :
    hoursOvertime = hours - 40
    grossPay = (40 * ratePerHour) + (hoursOvertime * ratePerHour * 1.5)
else :
    grossPay = hours * ratePerHour
    
print(f"Your total pay is ${grossPay}")
