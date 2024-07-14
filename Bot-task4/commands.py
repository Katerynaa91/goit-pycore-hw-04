"""Завдання 4. Модуль з функціями для скрипта task4main.py """

def parse_input(input_val: str) -> list:
    """Функція парсить рядок-запит, введений користувачем та обробляє випадок, якщо кількість 
    введених елементів не відповідає очікуваній структурі команди."""

    parsed_input = input_val.lower().split()
    if len(parsed_input) <= 3:
        return parsed_input
    return """Invalid request. Enter your request in the following format:
            - Add Name Phone
            - Change Name Phone
            - Show Name
            - All
            - Delete Name
            - Close or q (to close the program)"""

   

def add_contact(parsed_input_args: list, contacts_dict: dict):
    """Аргументи функції - введене значення без назви команди та словник контаків.
    Функція перевіріє, чи існує ім'я у словнику. Якщо не існує, створюється новий запис.
    Обробляється помилка, якщо кількість отриманих аргументів не відповідає очікуваній кількості. """

    try:
        if parsed_input_args[0] in contacts_dict.keys():
            print("Contact already exists. To create a new contact - use a different name")
        else: 
            contacts_dict.update({parsed_input_args[0]: parsed_input_args[1]})
            print("Contact added!")
    except IndexError:
        print("Incorrect format. Type your request in the format: Add Name Phone")
        
    

def change_contact(parsed_input_args:list, contacts_dict: dict):
    """Якщо ім'я, отримане у запиті користувача, відповідає ключу словника, функція змінює значення для 
    відповідного ключа"""

    if len(parsed_input_args) == 2 and contacts_dict.get(parsed_input_args[0]):
        contacts_dict[parsed_input_args[0]] = parsed_input_args[1]
        print("Contact updated!")
        
    else: 
        print("Name not found in contacts. If you want to add a new contact, please use 'add' command")
    
    
def show_phone(parsed_input_args:list, contacts_dict: dict):
    """Функція повертає пару ключ (ім'я контакта) - значення (номер телефона) відповідно до введеного запиту."""

    try:
        if parsed_input_args[0] not in contacts_dict or len(parsed_input_args) != 1:
            print("Contact not found")
            
        else:
            for key, value in contacts_dict.items():
                if parsed_input_args[0] == key:
                    print(key.capitalize(), value)
    except IndexError: 
        print("Incorrect format. Type your request in the format: Show Name")
                

def show_all(contacts_dict: dict):
    """Функція отримує словник контактів у якості параметра та повертає зміст цього словника."""

    if contacts_dict:
        for key, value in contacts_dict.items():
            print(key.capitalize(), value)
    else: print("Contacts list is empty.")


def delete_contact(parsed_input_args:list, contacts_dict: dict):
    
    """Функція видаляє запис зі словника відповідно до введеного запиту."""
    try:
        contacts_dict.pop(parsed_input_args[0])
        print("Contact deleted")
    except KeyError:
        print("Contact not found")
    except IndexError: 
        print("Incorrect format. Type your request in the format: Delete Name")



if __name__ == "__main__":
    pass