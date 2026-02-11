with open("products.csv", "w", encoding="utf-8") as file:
    file.write("Название;Цена;Количество\n"
               "Яблоки;100;50\n"
               "Бананы;80;30\n"
               "Молоко;120;20\n"
               "Хлеб;40;100\n")

with open("products.csv", "r", encoding="utf-8") as file:
    text = file.readlines()

header = text[0]
products = text[1:]

while True:
    print("1) Показать все товары")
    print("2) Добавить новый товар")
    print("3) Поиск товара по названию")
    print("4) Рассчитать общую стоимость склада")
    print("5) Сохранить и выйти")

    choice = input("Выберите действие 1-5:\n")

    if choice == "1":
        print("Текущий список:")
        for line in products:
            print(line.strip())

    elif choice == "2":
        name = input("Название товара:")
        price = input("Цена:")
        quantity = input("Количество:")
        products.append(f"{name};{price};{quantity}\n")
        print("Товар добавлен")

    elif choice == "3":
        search = input("Введите название для поиска:").lower()
        found = False
        for line in products:
            if search in line.lower():
                print(f"Найдено: {line.strip()}")
                found = True
                break
        if not found:
            print("Ничего не найдено.")

    elif choice == "4":
        total = 0
        for line in products:
            parts = line.strip().split(";")
            price = int(parts[1])
            quantity = int(parts[2])
            total += price * quantity
        print(f"Общая стоимость всех товаров: {total}")

    elif choice == "5":
        with open("products.csv", "w", encoding="utf-8") as file:
            file.write(header)
            for line in products:
                file.write(line)
        print("Данные сохранены в products.csv")
        break

    else:
        print("Неверный ввод, попробуйте снова.")