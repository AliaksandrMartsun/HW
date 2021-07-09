

def season(month_number):
    if month_number == 1 or month_number == 2 or month_number == 12:
        return "Это зима!"
    elif month_number == 3 or month_number == 4 or month_number == 5:
        return "Это весна!"
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return "Это лето!"
    elif month_number == 9 or month_number == 10 or month_number == 11:
        return "Это осень!"


n = 0
while n < 4:
    n += 1
    result = season(int(input("Enter number: ")))
    print(result)
