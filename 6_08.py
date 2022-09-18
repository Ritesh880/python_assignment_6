'''Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots'''

quar = "ax^2+bx+c"
a, b, c = int(input("enter the value of a ")), int(
    input("enter the value of b ")), int(input("enter the value of c"))
D = b**2-(4 * a*c)
if D > 0:
    print("real and distinct roots")
elif D < 0:
    print("imaginary roots ")
elif D == 0:
    print("real and equal roots ")
