with open("text.txt", "w", encoding="utf-8") as file:
    file.write("я хочу спать\n"
               "я плохо знаю питон\n"
               "я почистил зубы\n"
               "это строчка 4\n"
               "хочу спать\n")

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.readlines()

lines_text = len(text)
long_text = max(text, key=len)
words_text = sum(len(line.split()) for line in text)

print(f"Количество строк: {lines_text}")
print(f"Количество слов: {words_text}")
print(f"Самая длинная строка: {long_text}")
