import sys


def parse_input(inputted_data: list[str]):
    pass


def handler_input():
    # add_contact(), change_contact(), show_phone()
    pass


def main():
    print("Welcome to the assistant bot!")

    while True:
        inputted_data = input("Enter command: ").split()
        if inputted_data[0] == "exit":
            print("Goodbye!")
            break
        parse_input(inputted_data)
        handler_input()


if __name__ == "__main__":
    main()


# python main.py
# python main.py add Oleksii 459621475
