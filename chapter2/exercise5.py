"""  Exercise 5: Write a program which prompts the user for a Celsius temperature,
 convert the temperature to Fahrenheit, and print out the converted temperature """

def celsFahrConvert() :
    celsiusTemp = int(input("Enter Temperature (°c) : "))
    FahrenheitTemp = (celsiusTemp*(9/5))+32
    print(f"Temp : {FahrenheitTemp}")  



celsFahrConvert()