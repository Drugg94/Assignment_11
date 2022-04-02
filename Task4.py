# Function takes arguments and puts them into a dictionary then returns them
from cmath import sqrt


def AreaofShape(**args):
    return args

# Assigns equation as the dictionary that contains the args
equation=AreaofShape(a=4.172,b=9.131844,c=18,d=-3.5,e=11.2,f=4.6,g=7,h=2.91683)
# Creates a list of all values in equation so that they can be indexed
numberlist = list(equation.values())
# Assigns variables for combination of numbers in equation
a = (numberlist[0] + numberlist[1]) ** 3
b = numberlist[2]
c = numberlist[3]
d = numberlist[4] - numberlist[5]
e = (numberlist[6] - numberlist[7]) ** (-2/5)
# Takes the root of the equation in order to create the answer
solution = sqrt((a-b)/(c+d*e))
# Outputs the solution of the equation from the above math equation
print(solution)