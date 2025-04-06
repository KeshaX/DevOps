try:
    kilometers = float(input("Введите километры: "))
except ValueError:
    print("Ошибка!")
    exit()
print(f"{kilometers} км = {kilometers*1000:.2f} м")