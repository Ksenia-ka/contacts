import os
import json
import time

print("Добро пожаловать в базу данных контактов!")
username = input("Введите логин: ")
password = input("Введите пароль: ")

filename = f"{username}.json"
if os.path.exists(filename):
    with open(filename, 'r') as file:
        user_data = json.load(file)
        if user_data['password'] == password:
            print("Успешный вход в систему!")
        else:
            print("Неверный пароль! Программа завершена.")
            exit()
else:
    user_data = {'password': password, 'contacts': {}}
    with open(filename, 'w') as file:
        json.dump(user_data, file)
    print("Регистрация прошла успешно!")

while True:
    print("\nМеню:")
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Найти контакт")
    print("4. Показать все контакты")
    print("5. Выйти")

    choice = input("Выберите выполняемое действие (1-5): ")

    start_time = time.time()

    if choice == '1':
        name = input("Введите имя контакта: ")
        phone = input("Введите номер телефона: ")
        user_data['contacts'][name] = phone

        with open(filename, 'w') as file:
            json.dump(user_data, file)

        print(f"Контакт {name} добавлен.")


    elif choice == '2':
        name = input("Введите имя контакта, который хотите удалить: ")
        if name in user_data['contacts']:
            del user_data['contacts'][name]

            with open(filename, 'w') as file:
                json.dump(user_data, file)

            print(f"Контакт {name} удалён.")
        else:
            print(f"Контакт {name} не найден.")


    elif choice == '3':
        name = input("Введите имя контакта для поиска: ")
        if name in user_data['contacts']:
            print(f"{name}: {user_data['contacts'][name]}")
        else:
            print(f"Контакт {name} не найден.")


    elif choice == '4':
        if user_data['contacts']:
            print("Ваши контакты:")
            for name, phone in user_data['contacts'].items():
                print(f"{name}: {phone}")
        else:
            print("Контакты отсутствуют.")

    elif choice == '5':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")

    end_time = time.time()
    print(f"Время выполнения операции: {end_time - start_time:.6f} секунд.")