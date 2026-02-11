with open("students.txt", "w", encoding="utf-8") as file:
    file.write("Иванов Иван: 5,4,3,5\n"
               "Петров Петр: 4,3,4,4\n"
               "Сидорова Мария: 5,5,5,5\n")

best_student = ""
max_average = 0

with open("students.txt", "r", encoding="utf-8") as file:
    text = file.readlines()

with open("result.txt", "w", encoding="utf-8") as result:

    for line in text:
        name, assessments = line.strip().split(": ")
        average = sum(int(numbers) for numbers in assessments.split(",")) / len(assessments.split(","))
        if average > max_average:
            max_average = average
            best_student = name
        if average > 4.0:
            result.write(f"{name}: {average}\n")

print(f"Лучший студент: {best_student} со средним баллом {max_average}")

