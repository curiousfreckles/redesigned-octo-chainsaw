'''
	Программа, которая выводит на экран дополнительный код введенного с клавиатуры шестнадцатеричного числа на восемь разрядов.
'''

number = '0x' + (input("Input an 8-digit hexadecimal number: "))
print("Your number is: %s" % number[2::])

# перевернем все биты c помощью ^ XOR
mask = '0xFFFFFFFF'
number_rev = hex(int(number, 0) ^ int(mask, 0))
print("Your number reversed: %s" % number_rev[2::])

# добавим один шестнадцатиричный бит
bit = '0x00000001'
merci = hex(int(number_rev, 0) + int(bit, 0))
print("One-complement of your number: %s" % merci[2::])