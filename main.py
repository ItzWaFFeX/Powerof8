import math

def is_power_of_8(n):
    if n <= 0:
        return False
    return math.log(n, 8).is_integer()
number = int(input("Enter a number: "))
if is_power_of_8(number):
    print(f"{number} is a power of 8.")
else:
    print(f"{number} is not a power of 8.")
