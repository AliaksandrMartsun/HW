from datetime import datetime
from datetime import timedelta

table = []
while True:
    print("1 - Ввести данные о поезде",
          "2 - информация о всех поездах",
          "3 - инфа о поездах которые превышают 7 часов 20 минут",
          "4 - выход из программы")
    choice = int(input())
    if choice == 1:
        print("введите название ")
        info = {"Number": input(), "Arrived point": input(),
                "Arrival time": datetime.strptime(input("Введите время d/m/y h:m"), "%d/%m/%Y %H:%M"),
                "Destination": input("Введите время d/m/y h:m"),
                "Dop_time": datetime.strptime(input("Введите время d/m/y h:m"), "%d/%m/%Y %H:M")}
        info["Time in trip"] = info["Dop_time"] - info["Arrival time"]
        table.append(info)
    elif choice == 2:
        for i in table:
            print(i)
    elif choice == 3:
        for i in table:
            if i["Time in trip"] >= timedelta(hours=7, minutes=20):
                print(i)
    elif choice == 4:
        break
