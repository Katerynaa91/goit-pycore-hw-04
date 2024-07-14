"""Завдання 3. Розробити скрипт, який приймає шлях до директорії в якості аргументу 
командного рядка і візуалізує структуру цієї директорії, виводячи імена 
всіх піддиректорій та файлів. Імена директорій та файлів мають відрізнятися за кольором. 
Виконати обробку помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.
"""

from pathlib import Path
import sys
from colorama import init, deinit, Fore

init()

def scan_directories(path):
    """Функція отримує шлях до директорії як аргумент при запуску.
    Використовуються модулі pathlib - для рекурсивного обходу директорій та файлів,
    sys - для звернення до аргументів командного рядка,
    colorama - для надання кольору скрипту.
    """
    if path.exists():
        for file in path.iterdir():
            if file.is_file():
                print(Fore.GREEN + "• " + str(file.name), "\n")
        for folder in path.iterdir():
            if folder.is_dir():
                print(Fore.YELLOW + str(folder.name) + "\\", "\n")
                scan_directories(folder)
    else: 
        print("No such file!")


def get_path():
    sys_arguments = sys.argv
    dir_name = None if len(sys_arguments) <= 1 else sys_arguments[-1]
    return Path(dir_name)


if __name__ == "__main__":

    filename = get_path()
    scan_directories(filename)

    deinit()