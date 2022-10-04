#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_conversion(number):
    if number.isdigit():
        decimal = int(number)
        result = ""
        while decimal != 0:
            result = str(decimal%2) + result
            decimal = int(decimal/2)
        print(f'Десятичное число {number} = {result} в двоичной системе')
    else:
        print("Необходимо ввести число")

def input_figures():
    num = input('Введите десятичное число для преобразования в двоичное: ')
    binary_conversion(num)

input_figures()