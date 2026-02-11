with open("library.json", "w", encoding="utf-8") as file:
    file.write('''[
    {
        "id": 1,
        "title": "Мастер и Маргарита",
        "author": "Булгаков",
        "year": 1967,
        "available": true
      },
      {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Достоевский",
        "year": 1866,
        "available": false
      }
    ]''')

while True:
    with open("library.json", "r", encoding="utf-8") as file:
        text = file.read()

    books = []
    all_parts = text.split('{')
    for book_text in all_parts[1:]:
        if book_text.strip():
            book_data = book_text.split('}')[0]
            words = book_data.split()
            clean_book = " ".join(words)
            books.append(clean_book)

    print("1) Просмотр")
    print("2) Поиск")
    print("3) Добавить")
    print("4) Статус")
    print("5) Удалить")
    print("6) Экспорт")
    print("7) Выход")
    choice = input("Действие: ")

    if choice == "1":
        for change in books:
            print(change)

    elif choice == "2":
        search = input("Название или автор: ").lower()
        found = False
        for change in books:
            if search in change.lower():
                print(f"Найдено: {change.strip()}")
                found = True
                break

        if not found:
            print("Ничего не найдено.")

    elif choice == "3":
        new_id = len(books) + 1
        title = input("Название: ")
        author = input("Автор: ")
        year = input("Год: ")
        books.append(f'"id": {new_id}, "title": "{title}", "author": "{author}", "year": {year}, "available": true')
        with open("library.json", "w", encoding="utf-8") as file:
            formatted_books = ["{" + line + "}" for line in books]
            file.write("[\n  " + ",\n  ".join(formatted_books) + "\n]")

    elif choice == "4":
        temporary = input("ID для смены статуса: ")
        for i in range(len(books)):
            if f'"id": { temporary},' in books[i]:
                current = books[i]
                if "true" in current:
                    books[i] = current.replace("true", "false")
                else:
                    books[i] = current.replace("false", "true")
        with open("library.json", "w", encoding="utf-8") as file:
            formatted_books = ["{" + line + "}" for line in books]
            file.write("[\n  " + ",\n  ".join(formatted_books) + "\n]")

    elif choice == "5":
        temporary = input("ID для удаления: ")
        new_books = []
        for change in books:
            if f'"id": {temporary},' not in change:
                new_books.append(change)
        books = new_books
        with open("library.json", "w", encoding="utf-8") as file:
            formatted_books = ["{" + b + "}" for b in books]
            file.write("[\n  " + ",\n  ".join(formatted_books) + "\n]")

    elif choice == "6":
        with open("available_books.txt", "w", encoding="utf-8") as export_file:
            count = 0
            for change in books:
                if '"available": true' in change:
                    export_file.write(change + "\n")
                    count += 1
        print(f"Экспорт завершен. Записано книг: {count}")

    if choice == "7": break