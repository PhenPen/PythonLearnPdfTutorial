""" Exercise 3: Write a program to prompt the user for hours and rate per hour to
 compute gross pay."""

hours = float(input("Enter number of hours : "))
ratePerHour = float(input("Enter rate per hour :"))
grossPay = hours * ratePerHour
print(f"Your total pay is ${grossPay}")