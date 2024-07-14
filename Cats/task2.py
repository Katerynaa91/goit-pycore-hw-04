"""Завдання 2. Розробити функцію, яка читає файл з інформацією про котів та 
повертає список словників, де кожен словник містить інформацію про одного кота.
Опрацювати винятки, пов'язані з читанням файлу."""

from pathlib import Path


def get_cats_info(path: str) -> list:
    """Функція приймає один аргумент - шлях до текстового файлу (path).
    Функція повертає список словників з ключами "id", "name", "age".
    Наявність файла перевіряється за допомогою модуля pathlib."""

    if Path(path).exists():
        with open(path, "r", encoding="utf-8") as f:
            new_file = f.readlines()

        all_cats = list()
        one_cat = dict()

        for record in new_file:
            record = record.strip().split(',')
            one_cat["id"] = record[0]
            one_cat["name"] = record[1]
            one_cat["age"] = record[2]
            all_cats.append(one_cat)
            
        return all_cats
    return "File Not Found"
    

if __name__ == "__main__":

    wrong_file = "catsssss.txt"
    file = "Cats\\cats_data.txt"

    print(get_cats_info(file))
    print(get_cats_info(wrong_file))
