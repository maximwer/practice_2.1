print("Последние 5 операций")
try:
    with open("calculator.log", "r", encoding="utf-8") as file:
        lines = file.readlines()

    last = lines[-5:]
    for line in last:
        print(line.strip())
except FileNotFoundError:
    print("записей нету\n")

while True:
    print("1. Новое вычисление")
    print("2. Очистить лог-файл")
    print("3. Выйти")

    choice = input("Выберите действие (1-3): ")

    if choice == "1":
        try:

            number1 = input("Введите первое число: ")
            number2 = input("Введите второе число: ")
            operation = input("Введите операцию (+, -, *, /):")

            meaning1 = float(number1)
            meaning2 = float(number2)
            result = 0

        except ValueError:
            print("Ошибка: вводите числа и знаки а не текст")
            continue

        if operation == "+":
            result = meaning1 + meaning2
        elif operation == "-":
            result = meaning1 - meaning2
        elif operation == "*":
            result = meaning1 * meaning2
        elif operation == "/":
            if meaning2 != 0:
                result = meaning1 / meaning2
            else:
                print("Ошибка: деление на ноль!")
                continue

        print(f"Результат: {result}")

        log_entry = f"{number1} {operation} {number2} = {result}\n"
        with open("calculator.log", "a", encoding="utf-8") as file:
            file.write(log_entry)

    elif choice == "2":
        with open("calculator.log", "w", encoding="utf-8") as file:
            print("Лог-файл очищен!")

    elif choice == "3":
        print("До свидания!")
        break
    else:
        print("Неверный ввод.")