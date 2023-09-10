import datetime

year = int(input("Enter a year: "))

date_object = datetime.date(year, 2, 29)

try:
    date_object = date_object.strftime("%Y-%m-%d")
    print(f"{year} is a leap year.")
except ValueError:
    print(f"{year} is not a leap year.")