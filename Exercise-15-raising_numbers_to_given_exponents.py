# Pseudocode
# 1. Using def functions create a function called exponent(base,exp)
# 2. Return the int vaulue of base raises to the power of exp

# for defining exponent(base, exp)
def exponent(base, exp):
    exponent_number = exp
    result = 1
    while exponent_number > 0:
        result = result * base
        exponent_number = exponent_number - 1 
# for printing the result   
    print(base, "raised to", exp, "is: ", result)
# sample given
exponent(5, 4)