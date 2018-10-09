'''
	Логические операции
'''

f = True
g = False
print("f: ", f)
print("g: ", g)
print("not f: ", not f)
print("f and g = ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g: ", f != g)
print("\n")
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h <= i: ", 0 < h <= i)
print("\n\n")

'''
	Побитовые операции
'''
j = 7
k = 20
print("j = %d; j in binary format %s" % (j, bin(j)))
print("k = %d; k in binary format %s" % (k, bin(k)))
print("j & k: %d; binary %s" % (j & k, bin(j & k))) # побитовое AND
print("j | k: %d; binary %s" % (j | k, bin(j | k))) # побитовое OR
print("j ^ k: %d; binary %s" % (j ^ k, bin(j ^ k))) # побитовое XOR
print("~k: %d; binary: %s" % (~k, bin(~k))) # инверсия двоичного числа
print("k>>1: %d; binary: %s" % (k>>1, bin(k>>1))) # сдвиг на один бит вправо
print("k<<1: %d; binary: %s" % (k<<1, bin(k<<1))) # сдвиг на один бит влево
print("\n\n")

'''
	Шаг 9: дополнить код программы. Создать переменные А и В с неравными целочисленными значениями, переменные C и D со значениями True и False соответственно.
'''
A = 1
B = 3
C = True
D = False

'''
	Шаг 10: дополнить код программы, осуществить вывод на экран следующих операций: НЕ(C И D), С И D ИЛИ НЕ (C И D), НЕ(C ИЛИ D)
'''
print("C: ", C)
print("D: ", D)
print("not (C and D): ", not (C and D)) # НЕ(C И D)
print("C and D or not(C and D): ", C and D or not(C and D))# С И D ИЛИ НЕ (C И D)
print("not (C or D): ", not (C or D)) # НЕ(C ИЛИ D)
print("\n\n")

'''
	Шаг 11: дополнить код программы, осуществить вывод в консоль значений следующих выражений: A<=B, A>B and A==B, not (A<B)
'''
print("A: ", A)
print("B: ", B)
print("A <= B: ", A <= B) # A<=B
print("A > B and A == B: ", A > B and A == B)# A>B and A==B
print("not (A < B): ", not (A < B))# not (A<B)
print("\n\n")

'''
	Шаг 12: Дополнить код программы. Создать переменную s со значением 154 и переменную p со значением 6. Осуществить вывод ее значения в десятичном и двоичном виде на экран.

'''
s = 154
p = 6
print("s = %d; s in binary format %s" % (s, bin(s)))
print("p = %d; p in binary format %s" % (p, bin(p)))
'''
	Шаг 13: Дополнить код программы. Выполнить операцию побитового ИЛИ над переменными s и p с записью результата в переменную s. Осуществить вывод значения в десятичном и двоичном виде на экран. 
'''
s = s | p
print("s | p: %d; binary %s" % (s, bin(s))) # побитовое ИЛИ
'''
	Шаг 14: Дополнить код программы. Выполнить операцию побитового сдвига вправо на 2 бита над переменными s и p с записью результата в соответствующие переменные. Осуществить вывод значения в десятичном и двоичном виде на экран. 
'''
s = s >> 2
p = p >> 2
print("s>>2: %d; binary: %s" % (s, bin(s))) # сдвиг на один бит вправо
print("p>>2: %d; binary: %s" % (p, bin(p))) # сдвиг на один бит вправо
print("\n\n")