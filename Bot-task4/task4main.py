"""Завдання 4. Написати консольного бота, який розпізнаватиме команди, що вводяться з клавіатури,
 та буде відповідати відповідно до введеної команди. Бот повинен вміти зберігати ім'я та номер телефону, 
 знаходити номер телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, 
 які зберіг. Дані зберігаються у словнику, де ключ - ім'я користувача, значення - номер телефону."""

import commands

def main():
    """Фунцкія реалізує команди відповідно до запитів, введених з клавіатури. Нові дані зберігаються у словник.
    У функції використовується модуль commands, де визначається логіка окремої команди"""
    
    command_names = {
        "greeting": ["hi", "hello"],
        "add": ["add"],
        "change": ["change", "update"],
        "show": ["show", "view"],
        "show_all": ["all"],
        "close": ["close", "exit", "quit", "q", "bye"],
        "delete": ["remove", "delete", "del"]
    }

    phone_book = {}

    while True:
        user_input = input("Enter your request: ")
        command, *args = commands.parse_input(user_input)

        if command in command_names["greeting"]:
            print("Hi. How may I help you?")
        elif command in command_names["add"]:
            commands.add_contact(args, phone_book)
        elif command in command_names["change"]:
            commands.change_contact(args, phone_book)
        elif command in command_names["show"]:
            commands.show_phone(args, phone_book) 
        elif command in command_names["show_all"]:
            print("Type 'all' to check all contacts list") if args else commands.show_all(phone_book)
        elif command in command_names["delete"]:
            commands.delete_contact(args, phone_book)
        elif command in command_names["close"]:
            print("Bye!")
            break
        else: print("Invalid command")
  


if __name__ == "__main__":
    main()