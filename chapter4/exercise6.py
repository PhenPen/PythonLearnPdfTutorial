""" Exercise6 : Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate)."""

# Former pay computation index = 3.1

def compute_pay(hours :float,rate :float)  :
    if hours > 40 :
     hoursOvertime = hours - 40
     grossPay = (40 * rate) + (hoursOvertime * rate * 1.5)
    else :
     grossPay = hours * rate

    return f"Your total pay is ${grossPay}"
    

print(compute_pay(45,10))
            