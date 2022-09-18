'''Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part'''

complex = complex(input("enter a complex number "))
if complex.real > complex.imag:
    print("real part is greater ",complex.real)
else:
    print("imag part is greater ",complex.imag)
