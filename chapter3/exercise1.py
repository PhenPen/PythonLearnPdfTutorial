""" Exercise1 : Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours"""

# Former pay computation index = 2.3
while True :
    try :
        ratePerHour = float(input("Enter rate per hour :"))
    except ValueError :
        print("\n Enter a number for Rate per Hour")
    else :
        break

while True :
    try:
        hours = float(input("Enter number of hours : "))
    except ValueError:
        print("\n Enter a number for Hours ")
    else :
        break


if hours > 40 :
    hoursOvertime = hours - 40
    grossPay = (40 * ratePerHour) + (hoursOvertime * ratePerHour * 1.5)
else :
    grossPay = hours * ratePerHour
    
print(f"Your total pay is ${grossPay}")
