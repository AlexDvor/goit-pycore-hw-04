
from pathlib import Path

def total_salary(path:str):
	relative_path= Path(path)
	absolute_path = relative_path.absolute()
	some_num =[]
	total = None
	average= None

	try:
		with open(absolute_path,"r" ,encoding='utf-8') as file:
			items = file.readlines()

		for item in items:
			num= int(item.split(",")[1].strip())
			some_num.append(num)
		
		total = sum(some_num)
		average = total // len(items)
		return f"Загальна сумма заробітньої плати:{total}, Середня заробітня платня:{average} "
	
	except FileNotFoundError:
		print("File is not exist,try to use other path")

print(total_salary("./salary.txt"))

	



