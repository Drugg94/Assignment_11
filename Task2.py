# Function takes arguments and puts them into a dictionary then returns them
def AreaofShape(**args):
    return args

# Assigns cube as the dictionary that contains the args
cube=AreaofShape(volume = 729)
# iterates through cube calculating a cube's length with the arguments
for args in cube:
    length = (cube[args] ** (1/3))
# Outputs the length of a cube from the above function
print(length, "cm^3")