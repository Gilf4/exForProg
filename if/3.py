year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Количество дней в году:", 366)
else:
    print("Количество дней в году:", 365)