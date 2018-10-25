''' 
	Списки
'''

a = [1, 2, 3, 4, 5]
print("a[0]: ", a[0])
print("List a[0:5]: ", a[0:5])
print("List a[:]: ", a[:])
print("List a: ", a)
print("List a[1:5]: ", a[1:])
print("List a[0:4]: ", a[:4])
print("Length of list a: ", len(a))

print("\nList a (by index):")
# получение элементов списка в цикле (1)
for i in range(0,len(a)):
    print(a[i], end=" ")

print("\nList a (by elements):")
# получение элементов списка в цикле (2)
for elem in a:
    print(elem, end=" ")
print("\n")

b = []
b.append(20) # добавление элемента в конец
b.extend(a) # добавление элементов списка a в b
print("List b (extended): ", b)
b.insert(3,5) # добавить элемент на позицию
print("List b (insert element): ", b)
b.remove(5) # удалить первый элемент, равный 5
print("List b (remove element): ", b)
c1 = b.pop() # удалить и вернуть последний элемент
print("List b (pop last element): ", b)
print("c1: ", c1)
c2 = b.pop(3) # удалить и вернуть эл. с позиции
print("List b (pop 3rd element): ", b)
print("c2: ", c2)
bCopy = b.copy() # создать копию списка
print("List b: ", b)
print("List bCopy: ", bCopy)
b.reverse() # поменять элем. местами с конца в начало
print("List b (reversed): ", b)
b.sort(reverse=True) # сортировка элементов списка
print("List b (sorted): ", b)
b.clear(); # очистка списка
print("List b (cleared): ", b)
print("\n")

# сравнение списков
a1 = [1, 2, 4]
a2 = [1, 2, 3]
print("a1 == a2: ", a1 == a2)
a1.append(-1)
print("a1 == a2: ", a1 == a2)
print("a1 > a2: ", a1 > a2)
print("a1 < a2: ", a1 < a2)
print("\n\n")

'''
Шаг 9: Дополнить код программы lab_02_03.py. Создать список list1, заполненный 10 значениями, введенными с клавиатуры. Отсортировать список по убыванию, используя стандартную функцию, после чего вывести последние пять значений списка на экран.
'''
list1 = [int(x) for x in input("Type in any ten numbers split by a space: ").split()]
print("Now let's sort the list in reverse order!")
list1_reverse = list1.copy()
list1_reverse.sort(reverse=True)
print("Here is your list of numbers, sorted in reverse order: %s" % (" ".join(str(i) for i in list1_reverse)))
print("The last five elements of the new list: %s" % (" ".join(str(i) for i in list1_reverse[-5::])))

'''
Шаг 10: Дополнить код программы lab_02_03.py. Создать список list2, являющий копией списка list1, значения которого перенесены из конца списка в начало. Использовать стандартные функции. Вывести список list2 на экран до и после реверсирования значений.
'''

list2 = list1.copy()
print("Let's reverse the list again!")
print("Here is the list before reverse order sorting: %s" % " ". join(str(i) for i in list2))
list2.sort(reverse=True)
print("Here is the list of numbers, sorted in reverse order: %s" % " ". join(str(i) for i in list2))