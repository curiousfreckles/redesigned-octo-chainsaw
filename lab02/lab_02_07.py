'''
	Программа, которая преобразует введенное с клавиатуры двенадцатеричное число в систему с основанием 14 и выводит результат преобразования на экран.
'''

twelve = input("Type in any base-12 number to convert to base-14: ")

# переведем в десятичное число
decimal = int(twelve, 12)

# список для хранения остатков от деления
remains = []

while True:
	if decimal <= 14:
		remains.append(decimal)
		break
	remains.append(decimal % 14)
	decimal = decimal // 14

remains.reverse()

digits = '0123456789abcd'
fourteen = "".join([digits[i] for i in remains])
print("Your number in base-14: %s" % fourteen)