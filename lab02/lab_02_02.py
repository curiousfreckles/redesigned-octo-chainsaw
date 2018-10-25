'''
	 Циклы
'''
# while
print("Numbers < 10 (while):") 
i = 0
while (i < 10):
    print(i, end=" ") # print in one line
    i += 1
print("\n")

# for
print("Numbers < 10 (for):")
for i in range(0,10):
    print(i, end=" ")
else:
    print("\nThe next number is 10\n")
# break

sum = 0
for i in range(0, 100):
	if i > 10:
		print("\nWe reached the end, final sum: " ,sum)
		break
	sum += i

# continue 
i = 0
while i <= 15:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("\n")

# pass
print("Let's print numbers again!")
for i in range(0,10):
    pass
    print(i, end=" ")
print("\n\n")

'''
	Шаг 5: Дополнить код программы lab_02_02.py. Осуществить вывод на экран чисел в диапазоне от 0 до 500, кратных 7, с использованием двух видов циклов. По окончании работы циклов в блоке else вывести сообщение "All numbers were printed!".
'''

print("Let's print numbers divisible by 7! But let's skip the ones that are divisible by 14, though")
# Цикл continue 
i = 0
while True:
	if i == 300:
		break
	elif i % 7 == 0 and i % 2 != 0:
		print(i, end=" ")
	i += 1
	continue
else:
	print("\nAll numbers were printed!")
print("\n")

# Цикл pass
print("Let's print these numbers again!")
for i in range(0, 500):
	if i == 300:
		break
	elif i % 7 == 0 and i % 2 != 0:
		pass
		print(i, end=" ")
else: 
	print("\nAll numbers were printed!")
print("\n\n")


'''
Шаг 6: Дополнить код программы lab_02_02.py. Модифицировать написанные на предыдущем шаге циклы, добавив пропуск вывода значений кратных 14 и остановку цикла по достижении значения 300 (с помощью break).

(см. выше)
'''

'''
7. Дополните код программы lab_02_02.py. Осуществите вывод на экран следующей таблицы с использованием двух видов циклов:
1000
0200
0030
0004
'''

# Поэлементно с помощью while 
row, col = 0, 0
matrix = ""

while row <= 3:
	# Если главная диагональ добавляем номер строки
	if row == col:
		matrix += str(col + 1)
	# Иначе просто ноль
	else:
		matrix += "0"
	
	col += 1
	
	if col == 4:
		col = 0
		row += 1
		matrix += "\n"
print(matrix)


# Построчно с помощью for
for a in range(4):
	row = ["0"] * 4 # четыре нуля
	row[a] = str(a + 1)
	print("".join(row))





