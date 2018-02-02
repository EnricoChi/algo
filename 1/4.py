# 4. Написать программу, которая генерирует в указанных пользователем границах
#
# -случайное целое число,
# -случайное вещественное число,
# -случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


# Предлагаем выбрать из списка
# 1 генерирует целое
# 2 генерирует вещественное
# 3 генерирует символ

# Инпут1

# Проверяем ввод
# Если1 = 1
# инпут2 целого числа
# Если1 = 2
# инпут2 вещественного числа
# Если1 = 3
# инпут2 символов

# Если инпут1 == 1
#   Если инпут2 не содержит символы кроме целых чисел
#       рандом инпут2[0], инпут2[1]
#   Иначе
#       начинаем инпут2 сначала

# Если инпут1 == 2
#   Если инпут2 не содержит символы кроме целых чисел
#       рандом инпут2[0], инпут2[1]
#   Иначе
#       начинаем инпут2 сначала

# Если инпут1 == 3
#   Если инпут2 не содержит символы кроме букв
#       рандом инпут2[0], инпут2[1]
#   Иначе
#       начинаем инпут2 сначала

import random


# Операции с введёнными числами
def value_input(input_type, actions_title):
    try:
        print('Укажите диапазон, чтобы генерировать {}:'.format(actions_title[input_type]))
    except KeyError:
        print('\n*** Ничего не выйдет ***\n')
    else:
        if input_type == '1':
            item_range = [int(item) for item in input('Через запятую ~ 1,2: ').split(',')]
            if item_range:
                print('Нагенерил {} = {}\n'.format(actions_title[input_type],
                                                   random.randint(item_range[0], item_range[1])))  # Рандом
        elif input_type == '2':
            item_range = [int(item) for item in input('Через запятую ~ 1,2: ').split(',')]
            if item_range:
                print('Нагенерил {} = {}\n'.format(actions_title[input_type],
                                                   random.uniform(item_range[0], item_range[1])))  # Рандом
        elif input_type == '3':
            item_range = [item for item in input('Через запятую ~ a,f: ').split(',')]
            if item_range:
                abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                # Через срез + 1, чтобы включить последний символ
                print('Нагенерил {} = {}\n'.format(actions_title[input_type],
                                                   random.choice(
                                                       abc[abc.find(item_range[0]):abc.find(item_range[1]) + 1])))


while True:
    # Обьявим варианты
    actions_title = {'1': 'целое число',
                     '2': 'вещественное число',
                     '3': 'символ'}
    # Покажем варианты
    for title in actions_title:
        print('Введите {} чтобы генерировать {}'.format(title, actions_title[title]))

    # Примем число в качестве варианта
    input_type = input('1|2|3?: ')

    # Если получили число, то обрабатываем. Иначе сначала
    if input_type:
        value_input(input_type, actions_title)
    else:
        print('\nНе верный ввод, повторите попытку!')
        continue
