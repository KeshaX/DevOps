name = input("Введите свое имя: ").strip().capitalize()
print(f"Здравствуйте, {name}")


login = input("Введите логин: ").strip().capitalize()
password = input("Введмте пароль: ").strip()
if password.isnumeric():
    password = int(password)
    if login == "Admin" and password == 1234:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")
else:
    print("Пароль должен быть числом!")
