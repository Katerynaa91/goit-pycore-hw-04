"""Завдання 1. Розробити функцію, яка аналізує файл з заробітними платами всіх розробників
і повертає загальну та середню суму заробітної плати всіх розробників. Результатом роботи функції 
є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
Опрацювати можливі винятки при роботі з файлами, коли файл відсутній або пошкоджений."""

from pathlib import Path

def total_salary(path: str) -> tuple:
    """Параметром функції є шлях до файлу. Функція повертає кортеж з двох чисел з плаваючою крапкою.
    Наявність файла перевіряється за допомогою модуля pathlib."""

    if Path(path).exists():
        with open(path, "r", encoding="utf-8") as f:
            new_file = f.readlines()
            salaries_lst = list()
            for record in new_file:
                salary = record.strip().split(',')[1]
                salaries_lst.append(float(salary))
            total_salary = sum(salaries_lst)
            medium_salary = sum(salaries_lst)/len(salaries_lst)

        return total_salary, medium_salary
    return "Incorrect File Name"
    


if __name__ == "__main__":
    file = R"Salaries\salaries_data.txt"
    no_file = "no_file.txt"

    print(total_salary(file))
    print(total_salary(no_file))