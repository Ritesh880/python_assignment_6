#Write a python script to check whether a given year is a leap year or not.
year=int(input("enter year"))
if year%400==0:
    print("entered year is leap year ")
else:
    print("entered year is not a leap year")    