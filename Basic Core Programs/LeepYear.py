def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a 4-digit year: "))

if 1000 <= year <= 9999:
    if is_leap_year(year):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")
else:
    print("Please enter a valid 4-digit year.")
