""" """


while True:
    try:
        fahr = float(input("Enter Fahrenheit Temperature:"))
    except ValueError:
     print("Enter a valid number ")
    else:
       cel = (fahr- 32.0) * 5.0 / 9.0
       print("The temperature in Celsius is :", cel)
       break
    finally :
       print("Program by Phen")
