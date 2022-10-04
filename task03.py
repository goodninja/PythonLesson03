# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import re

def float_checking(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

def list_checking(array):
    i = 0
    check = True
    while check and i<len(array):
        check = float_checking(array[i])
        i += 1
    return check

def minmax_difference(numbers):
    numbers_list = numbers.split(" ")
    if list_checking(numbers_list):
        searching_list = list(map(lambda x: re.sub(r'\d+\.', "0.", x),numbers_list))
        searching_list = list(map(float,searching_list))
        searching_list = list(filter(lambda x: x<1, searching_list))
        print(f'Список дробных частей элементов: {searching_list}')
        result = max(searching_list) - min(searching_list)
        print(f'Разница между максимальным и минимальным значением дробной части элементов = {result}')
    else:
        print("Список должен состоять из чисел")

def input_figures():
    list = input('Введите вещественные числа, используя пробел: ')
    minmax_difference(list)

input_figures()