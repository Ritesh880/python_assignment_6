'''10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.'''

a, b, c = int(input("enter a number")), int(
    input("enter second number")), int(input("enter third number "))
if a > b and a > c:
    print("greater number is ", a)
elif b > a and b > c:
    print("greater number is ", b)
elif a == b and a == c:
    print("even")
else:
    print("greater number is ", c)
