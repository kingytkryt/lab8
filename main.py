# Лагода Тимофій
def main():
    filename = "questions.txt"
    try:
        with open(filename, "w") as file:#відкриття файлу
            #запис даних до файлу
            file.write("Студент: Лагода Тимофій\n")
            file.write("Питання: Що таке функція?\n")
        print(f"Файл '{filename}' успішно створено та заповнено.")
    except:
        print("Помилка: файл не знайдено або неможливо створити.")

#виклик головної функції
main()