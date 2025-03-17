import sys

contacts = []


def add_contact(name: str, phone: str):
    contacts.append({"name": name, "phone": phone})
    print("Contact added!")
    print(contacts)


def change_contact(name: str, phone: str):
    pass


def show_phone(name: str):
    for contact in contacts:
        if contact["name"] == name:
            print(contact["phone"])
            return
    print("Contact not found!")


def parse_input(inputted_data: list[str]):
    command = inputted_data[1:]
    return command


def handler_input(command_list: list[str]):
    match command_list:
        case ["add", name, phone]:
            add_contact(name, phone)
        case ["change", name, phone]:
            change_contact(name, phone)
        case ["show", name]:
            show_phone(name)
        case ["exit"] | ["close"]:
            print("Goodbye!")
            return
        case _:
            print("Invalid command!")


def main():
    print("Welcome to the assistant bot!")
    command = parse_input(sys.argv)
    while True:
        if command in ["exit", "close"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif len(command) == 3:
            handler_input(command)

        else:
            print("Invalid command!")
            break


# python main.py show Oleksii
# python main.py add Oleksii 459621475


if __name__ == "__main__":
    main()
