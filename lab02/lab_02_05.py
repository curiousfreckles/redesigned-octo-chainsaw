'''
14. Создайте программу lab_02_05.py, которая выводит на экран все возможные уникальные строки, составленные из символов строки введенной с клавиатуры.

'''
import itertools

string = input("Type in anything you like: ")
print(string)

# Все перестановки(комбинации без повторения)
permutations = list(map("".join, itertools.permutations(string)))
print("Here all the possible unique permutations: ")
print("\n". join(permutations))

# Без itertools