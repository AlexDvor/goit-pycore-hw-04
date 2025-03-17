from utils.collections_fun import add_contact, change_contact, show_all, show_phone

contacts = {}


def parse_input(inputted_data: str):
    command = inputted_data.split()
    command = [word.lower().strip() for word in command]
    return command


def handler_input(command_list: list[str]):
    match command_list:
        case ["add", name, phone]:
            add_contact(name, phone, contacts)
        case ["change", name, phone]:
            change_contact(name, phone, contacts)
        case ["show", name]:
            show_phone(name, contacts)
        case ["all"]:
            show_all(contacts)
        case _:
            print("Invalid command!")


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command = parse_input(user_input)

        if command in [["exit"], ["close"]]:
            print("Goodbye!")
            break
        elif command == ["hello"]:
            print("How can I help you?")
        else:
            handler_input(command)


if __name__ == "__main__":
    main()


"""
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.

☝ Бот помічник повинен стати для нас прототипом застосунку-асистента, який ми розробимо в наступних домашніх завданнях. Застосунок-асистент в першому наближенні повинен вміти працювати з книгою контактів та календарем.


У цій домашній роботі зосередимося на інтерфейсі самого бота. Найпростіший і найзручніший на початковому етапі розробки інтерфейс - це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати.

Будь-який CLI складається з трьох основних елементів:

Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.


На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.



Вимоги до завдання:

Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. В разі введення команди "exit" або "close", програма повинна завершувати виконання.
Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.


Рекомендації для виконання

По перше, нам треба систематизувати опис форматів наших команд для консольного бота-помічника. Це допоможе зрозуміти які функції треба зробити для кожної команди. Зробімо це:

1. Команда "hello", тут можна обійтись поки без функції та використати звичайний print:

Введення: "hello"
Вивід: "How can I help you?"


2. Команда "add [ім'я] [номер телефону]". Для цієї команди зробимо функцію add_contact:

Введення: "add John 1234567890"
Вивід: "Contact added."


3. Команда "change [ім'я] [новий номер телефону]". Для цієї команди зробимо функцію change_contact:

Введення: "change John 0987654321"
Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено


4. Команда "phone [ім'я]". Для цієї команди зробимо функцію show_phone:

Введення: "phone John"
Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено


5. Команда "all". Для цієї команди зробимо функцію show_all:

Введення: "all"
Вивід: усі збережені контакти з номерами телефонів


6. Команда "close" або "exit". Оскільки тут треба перервати виконання програми, можна поки обійтись без функції для цих команд:

Введення: будь-яке з цих слів
Вивід: "Good bye!" та завершення роботи бота
Будь-яка команда, яка не відповідає вищезазначеним форматам, буде вважатися нами невірною, і бот буде виводити повідомлення "Invalid command."



Почнемо з простого варіанту CLI-бота:

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



Коли програма запускається, вона виводить повідомлення "Welcome to the assistant bot!" і входить в нескінчений цикл, де вона очікує введення команди від користувача while True.



Якщо користувач вводить "close" або "exit", програма виводить "Good bye!" та завершує роботу. За це відповідає блок коду:

if command in ["close", "exit"]:
    print("Good bye!")
    break



Якщо користувач вводить "hello", програма виводить "How can I help you?". Якщо ж введена команда не відповідає жодному з цих варіантів, програма виводить "Invalid command.".

Welcome to the assistant bot!
Enter a command: test
Invalid command.
Enter a command: hello
How can I help you?
Enter a command: exit
Good bye!



Цей код створює простий інтерактивний командний рядок, який реагує на обмежений набір команд. Ми реалізували цикл запит-відповідь, який буде служити відмінною основою для додавання функціональності в майбутніх домашніх завданнях.



Тепер додамо парсер команд. Перепишемо наш код наступним чином

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



Ми додали функцію parse_input(user_input) яка приймає рядок вводу користувача user_input і розбиває його на слова за допомогою методу split(). Вона повертає перше слово як команду cmd та решту як список аргументів *args. Рядок коду cmd, *args = user_input.split() розділяє рядок на слова. Перше слово зберігається у змінній cmd, а решта зберігається у списку args завдяки оператору розпакування *. Далі рядок коду cmd = cmd.strip().lower() видаляє зайві пробіли навколо команди та перетворює її на нижній регістр.



☝ Навіщо приводити команду до нижнього регістру?

Припустимо, користувач вводить команду як "HELLO", "Hello" або "hello". Якщо не привести ці варіанти до спільного регістру, вони будуть розглядатися як різні команди, і вам доведеться обробляти кожний варіант окремо.

Приведення команди до нижнього регістру дозволяє уникнути цього, перетворюючи всі варіанти на одну та ту ж форму. Таким чином, ви можете легко порівнювати введену команду з попередньо визначеними командами без зважання на те, як користувач ввів її.
Це забезпечує кращий досвід користувача, оскільки програма стає менш чутливою до конкретного способу введення команд.


Отриманий результат в функції main ми отримаємо після виконання рядка коду command, *args = parse_input(user_input) .



Функція parse_input розбиває введений рядок на слова, використовуючи пробіл як розділювач. Змінна command отримує перше значення та вважається командою, а змінна args стає списком з усіх інших значень.



Наприклад, якщо ми введемо команду "add John 123456" то змінна command стане рядком "add" а змінна args стане списком ["John", "123456"] . Якщо ж ми введемо команду "hello" то command стане рядком "hello", а args буде пустим списком []



Маємо надію, ви вже зрозуміли тепер принцип парсера, настав час додати команду add.

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



Ми додали словник з контактами contacts = {} в середину функції main та функцію обробник команди add_contact.



Функція add_contact призначена для додавання нового контакту до словника контактів. Вона приймає два аргументи: args, який є списком і містить ім'я та телефонний номер, та contacts, який є словником, де зберігаються контакти.



Всередині функції, два елементи зі списку args розпаковуються в змінні name та phone. Функція далі додає пару "ключ: значення" до словника контактів, використовуючи ім'я як ключ і телефонний номер як значення contacts[name] = phone.

☝ Треба зауважити, що, якщо контакт з таким ім'ям вже існує, його дані будуть перезаписані без будь-яких попереджень. Тут ви вже можете діяти на свій розсуд, хочете чи ні ви обробляти колізію, в нашому варіанті ми перезаписуємо контакт.


Функція add_contact повертає рядок, що підтверджує успішне додавання контакту: "Contact added.".



Необхідно зауважити, що ця функція не має вбудованих перевірок на помилки введення. Наприклад, якщо args не містить двох елементів, ця функція викличе помилку ValueError.

ValueError: not enough values to unpack (expected 2, got 0)



Обробку помилок в цьому домашньому завданні залиште на свій розсуд, бо в наступному домашньому завданні ми додамо обробку помилок через декоратори.



Критерії оцінювання:

Бот повинен перебувати в нескінченному циклі, чекаючи команди користувача.
Бот завершує свою роботу, якщо зустрічає слова: "close" або "exit".
Бот не чутливий до регістру введених команд.
Бот приймає команди:
"hello", та відповідає у консоль повідомленням "How can I help you?"
"add username phone". За цією командою бот зберігає у пам'яті, наприклад у словнику, новий контакт. Користувач вводить ім'я username та номер телефону phone, обов'язково через пробіл.
"change username phone". За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику.
"phone username" За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.
"all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"close", "exit" за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль повідомлення "Good bye!" та завершить своє виконання.
Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.
Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.




"""
