from cmath import pi

# Function takes arguments and puts them into a dictionary then returns them
def AreaofShape(**args):
    return args

# Assigns circle as the dictionary that contains the args
circle=AreaofShape(radius = 5)
# iterates through circle calculating a circles area with the arguments
for args in circle:
    area = (pi * (circle[args] ** 2))
# Outputs the area of a circle from the above function
print(area)
