print("Привет, выберите опцию")
print("1. Прочесть файл")
print("2. Добавить запись")
print("3. Выйти")
print("created by Ayras")
while True:
    options = int(input("Выберите опцию: "))
    if options == 1:
        print("OPTIONS 1 selected")
        with open("content.txt", "r", encoding="utf-8") as document:
            text = document.read()
        print(text)

    elif options == 2:
        print("OPTIONS 2 selected")
        while True:
            name = input("Введите имя: \t\t")
            fam = input("Введите фамилию: \t")
            address = input("Введите ваш адрес:\t")
            data = f"{name}  {fam}  {address} \n"
            print(data)
            with open('content.txt', 'a', encoding='utf-8') as file:    # r - read; w - write; a - append
                file.write(data)
            msg = input("Добавить еще запись? yes/no: ")
            if msg == "yes":
                continue
            elif msg == "no":
                break

    elif options == 3:
        break

print("\nGoodbye")