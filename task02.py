# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiplication_of_numbers(numbers):
    if numbers.replace(" ", "").isdigit():
        numbers_list = numbers.split(" ")
        multiplication_list = list(map(int,numbers_list))
        result=[]
        i = 0
        while i<len(multiplication_list)/2:
            result.append(multiplication_list[i]*multiplication_list[len(multiplication_list)-1-i])
            i+=1
        print(f'Произведение пар чисел списка = {result}')
    else:
        print("Список должен состоять из чисел")

def input_figures():
    list = input('Введите числа, используя пробел: ')
    multiplication_of_numbers(list)

input_figures()