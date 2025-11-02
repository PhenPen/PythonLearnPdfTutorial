from tempConvertLib.convTemp import celsFahrConvert, celsKelvConvert, fahrCelsConvert, fahrKelvConvert, kelvCelsConvert, kelvFahrConvert

from exercise5bonus import unit

def selectTempConv() :
    match unit : 
        case "c" :
            unitInput = input("Convert to Fahrenheit or Kelvin ? : ").lower()
            if unitInput == "f" :
                print(celsFahrConvert())
            elif unitInput == "k" :
                print(celsKelvConvert())
            else :
                print("Invalid Input")

        case "f" :
            unitInput = input("Convert to Celsius or Kelvin ? : ").lower()
            if unitInput == "c" :
                print(fahrCelsConvert())
            elif unitInput == "k" :
                print(fahrKelvConvert())
            else :
                print("Invalid Input")

        case "k" :
            unitInput = input("Convert to Celsius or Fahrenheit ? : ").lower()
            if unitInput == "c" :
                print(kelvCelsConvert())
            elif unitInput == "f" :
                tempValueOut = kelvFahrConvert()
            else :
                print("Invalid Input")
