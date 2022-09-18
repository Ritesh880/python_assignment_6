# Write a python script to take the month value in numeric format and display the
# number of days in it.

month = int(input("Enter month value "))
if month == 2:
    print("28 days")
elif month == 1 or 3 or  5 or 7 or 8 or 10 or 12:
    print("31 days ")
elif month == 9 or 11 or 4 or 6:
    print("30 days ")
