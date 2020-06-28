# Interest program
# interest.py

# Author: Ramisha Malik


from math import exp

def simpleInterest(P, r, t):
    I = P*r*t   #I has local scope
    I = str(round(I, 2))
    return I

def compoundInterest(P, r, t, n):
    A = P*(1+r/n)**(n*t)
    I = A - P
    I = str(round(I, 2))
    return I
    
def continuousCompoundInterset(P, r, t):
    A = P*exp(r*t)
    I = A - P
    I = str(round(I, 2))
    return I

def main():
    Principal = eval(input("Please enter the amount you wish to invest:   "))
    ratePercent = eval(input("Please enter in percent, your rate of interest:   "))
    rate = ratePercent/100
    time = eval(input("Please enter number of years of investment:   "))
    kindOfInterest  = input("Please let us know the kind of interest you want (S for simple, C for compound, CC for continuousCompound):   ")
    if kindOfInterest == 'C':
        number = int(input("Please enter number of times you want to compound each year.  "))

    if kindOfInterest == 'S':
        print(f"Simple interest is ${simpleInterest(Principal, rate, time)}.")
    elif kindOfInterest == 'C':
        print(f"Compound interest compounded monthly is ${compoundInterest(Principal, rate, time, number)}.")
    elif kindOfInterest == 'CC':
        print(f"Compound interest compounded continuous is ${continuousCompoundInterset(Principal, rate, time)}.")
