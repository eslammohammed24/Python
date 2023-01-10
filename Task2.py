def leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        leap = False
        return leap


year = int(input("enter a year: "))
print(leap_year(year))
