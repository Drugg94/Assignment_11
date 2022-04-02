# Function takes arguments and puts them into a dictionary then returns them
def AreaofShape(**args):
    return args

# Assigns triangle as the dictionary that contains the args
triangle=AreaofShape(a = 10, b = 18)
# iterates through triangle calculating a triangle's hypotenuse with the arguments
hypotenuse = 0
for args in triangle:
    hypotenuse = (triangle[args] ** 2) + hypotenuse
hypotenuse = hypotenuse ** (1/2)
# Outputs the hypotenuse of a right triangle from the above function
print(hypotenuse)