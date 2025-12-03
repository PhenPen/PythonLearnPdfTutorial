""" Exercise 7: Rewrite the grade program from the previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade as a
string."""

#Former index : 3.3
def compute_grade(score : float) :
    if score >= 1.0 :
        return "Bad score"
    elif score >= 0.9 :
        return "A"
    elif score >= 0.8 :
        return "B"
    elif score >= 0.7 :
        return "C"
    elif score >= 0.6 :
        return "D"
    elif score < 0.6 :
        return "F"
    else :
        return "Bad Score"

while True : 
    try:
        grade = int(input("Enter grade : "))
    except ValueError :
        print("Enter only numbers for grade")
    else : 
        print(compute_grade(grade))
        break