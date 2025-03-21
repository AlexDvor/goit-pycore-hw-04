from pathlib import Path
from colorama import Fore, Style


def print_directory_structure(directory: Path, indent=0):

    if not directory.is_dir():
        print(f"{Fore.RED}Помилка: {directory} не є директорією.{Style.RESET_ALL}")
        return

    for item in sorted(directory.iterdir()):
        prefix = " " * (indent * 2)

        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}[DIR] {item.name}{Style.RESET_ALL}")
            print_directory_structure(item, indent + 1)
        else:
            print(f"{prefix}{Fore.GREEN}[FILE] {item.name}{Style.RESET_ALL}")


"""
iterdir() — це метод з модуля pathlib в Python. Він використовується для ітерації через вміст директорії (папки) та 
повертає генератор, який містить об'єкти типу Path для кожного елемента в папці (файлів або підпапок).

iterdir() проходить по всіх елементах у директорії, але не заходить у вкладені папки (не рекурсивно).

"""
