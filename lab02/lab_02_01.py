'''
	Условия
'''

#if..else
num = int(input("How many times have you been to the Hermitage? "))
if num > 0:
	print("Wonderful")
	print("I hope you liked this museum!")
else:
	print("You should definitely visit the Hermitage!")

#if..elif..else
course = int(input("What is your course number?"))
if course == 1:
	print("You are just at the beginning!")
elif course == 2:
	print("You learned many thigs, but not all of them!")
elif course == 3:
	print("The basic course is over, it's time for professional disciplines!")
else:
	print("Oh! You need to hurry! June is the month of thesis defense")

x = 5
y = 12

if y % x > 0 : print("%d cannot be evenly divided by %d" % (y,x))

z = 3
x = "{} is the divider of {}".format(z,y) if y%z==0 else "{} is not a divider of {}".format(z, y)
print(x)
print("\n\n")

'''
	Шаг 2: Дополнить код программы. Создать переменную р, в которую будет записано значение количества выполненных за год лабораторных поразличным дисциплинам. Осуществите вывод значения переменной в терминал, если значение больше 10. Оператор ветвления записать двумя способами: в одну строку и в несколько строк.
'''

p = int(input("How many labs have you already handed in this year? "))
# вариант в несколько строк
if p > 10:
	print("Wow! %d labs already, keep going, you're doing great!" % p)

# вариант в одну строку
if p > 10: print(p) 

'''
	Шаг 3: Дополнить код программы, создав переменные a со значением 157 и b со значением 525. Осуществить проверку следующих условий и выполнение соответствующих действий:
		-если a>b, рассчитать остаток от деления a на b и вывести значение на экран;
		-если a<b, рассчитать остаток от деления b на a и вывести значение на экран;
		-если a==b, рассчитать произведение чисел a и b и вывести значение на экран.
	Осуществить проверку, изменяя значения переменных в соответствии с условиями.
'''

a = 3
b = 3

print("Значения a и b: %d и %d, соответственно" % (a, b))

if a > b:
	print("a > b, рассчитаем остаток от деления a на b: %d" % (a % b))
elif b > a:
	print("b > a, рассчитаем остаток от деления b на a: %d" % (b % a)) 
elif a == b:
	print("a и b равны, рассчитаем произведение a и b: %d" % (a * b)) 




