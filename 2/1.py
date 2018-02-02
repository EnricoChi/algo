# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.

# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.

# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.

# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


# проверки должны быть сконцентрированы на границе системы,
# а не быть размазанными по телу функции (или в вашем случае программы).
# То есть длину введенного числа вы должны проверять сразу там же рядом с input(),
# потом его валидность, потом делать конвертацию, а потом вычисления


import re


# Исключение для неверных символов
class WrongItem(Exception):
    def __init__(self, item):
        self.item = item

    def __str__(self):
        return '--- {} не верное значение ---'.format(self.item)


# Сама математическая операция
def operation(a, b, operator):
    # Так наверное не правильно делать и лучше через if operator == '*'?
    str_format = '{}{}{}'.format(a, operator, b)
    try:
        # Просто выполняю строку
        result = eval(str_format)
        return result
    except ZeroDivisionError as e:
        return e


# Валидатор для чисел
def num_validate(item):
    """
    Поэтому лучше просто кидать ошибку, если хотя бы одно значение из пачки неверное.
    """
    # Не уверен что знаю как кидать ошибки, но попробую так
    try:
        # Регуляркой ищу всё кроме чисел и если найду, то буду кидать ошибку
        wrong_item = re.findall(r'[\D]', item)
        if wrong_item:
            raise WrongItem(wrong_item)
    except WrongItem as e:
        return 'error', e

    return item

    # Или так?
    # wrong_item = re.findall(r'[\D]', item)
    # if wrong_item:
    #     raise WrongItem(wrong_item)


# Валидатор для знаков
def operator_validate(item):
    try:
        # Ищу всё кроме допустимых знаков */+-
        wrong_item = re.findall(r'[^*/+-]', item)
        if wrong_item:
            raise WrongItem(wrong_item)
    except WrongItem as e:
        return 'error', e

    return item


# Ввод с клавиотуры
def key_input(type, num=None):
    while True:
        # Если число
        if num:
            item = input('Введите {} {}: '.format(type, num))
            item = num_validate(item)
            # Если валидация вернёт словарь, значит не прошло валидацию. Костыль?
            if isinstance(item, tuple) is not True:
                item = int(item)
                return item
            else:
                print(item[1])
        # Если не число
        else:
            item = input('Введите {}: '.format(type))
            if item == '0':
                return False
            else:
                item = operator_validate(item)
                if isinstance(item, tuple) is not True:
                    return item
                else:
                    print(item[1])


while True:
    # Запрос с клавиотуры, наличие второго аргумента будет означать что на ввод должно приходить число
    a = key_input('число', 'a')
    b = key_input('число', 'b')
    operator = key_input('оператор')

    # False вернёт key_input() вслучае если оператор будет == 0
    if operator is False:
        print('--- exit ---')
        break
    else:
        result = operation(a, b, operator)
        print('{} {} {} = {}\n'.format(a, operator, b, result))
