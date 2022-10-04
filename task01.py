# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def odd_position_summary(numbers):
    if numbers.replace(" ", "").isdigit():
        list_of_numbers = numbers.split(" ")
        sum = 0
        for i in range(1,len(list_of_numbers),2):
            sum += int(list_of_numbers[i])
        print(f'Сумма элементов списка, стоящих на нечётной позиции = {sum}')
    else:
        print("Список должен состоять из чисел")

def input_figures():
    list = input('Введите числа, используя пробел: ')
    odd_position_summary(list)

input_figures()