from pathlib import Path


def get_cats_info(path:str)-> list[dict[str, str]]:
	absolute_path = Path(path).absolute()
	cats_data=[]

	try:
		with open(absolute_path, "r", encoding="utf-8") as file:

			for item in file:
					cat_info = item.strip().split(",")
					if len(cat_info)!= 3 :
						print(f"Some error in line: {item.strip()} – missing")
						continue

					new_info={
						"id": cat_info[0],
						"name":cat_info[1],
						"age":cat_info[2],
					}
					cats_data.append(new_info)
		
		return cats_data
		
	except FileNotFoundError:
		print("File is not exist,try to use other path")


print(get_cats_info("./Task_2/animals.txt"))




"""
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.



Вимоги до завдання:

Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


Рекомендації для виконання:

Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.


Критерії оцінювання:

Функція має точно обробляти дані та повертати правильний список словників.
Повинна бути належна обробка винятків і помилок.
Код має бути чистим, добре структурованим і зрозумілим.


Приклад використання функції:

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)



Очікуваний результат:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]

"""


