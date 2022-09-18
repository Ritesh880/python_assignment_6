'''Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.'''
a = int(input("enter first number "))
b = int(input("enter second number "))
if a > b:
    print("greater numbe is ", a)
elif b > a:
    print("greater number is ", b)
elif a == b:
    print("even")
