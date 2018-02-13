# Задание 1.
# Реализовать функцию, которая на вход принимает данные о телефонных операторах (в виде сортированного списка таплов)
# и номер телефона (в виде строки). Функция должна вернуть оператора для этого номера.
# Данные об операторах представляют собой сортированный список из таплов следующего вида:
# ('7123456789', '7222111000', 'имя-оператора').
#
# Реализовать функцию: def get_operator(operators, number), сложность O(log N).
#
# Пример:
#
from bisect import bisect_left
import itertools

operators_data = [('7111111111', '7111222222', 'operator-1'),
                  ('7333333333', '7333333333', 'operator-2'),
                  ('744444444444', '7555555555', 'operator-1')]


# Без бисеката
def get_operator(operators, number):
    for i in operators:
        search_str = set(i)
        num = len(i)
        if number in search_str:
            return i[num-1]


# Через bisect
def get_operator_bisect(operators, number):
    # operators.sort(key=lambda r: r[1])
    # Бедм делать списки из таплов, и удалять оператора, чтобы раскатать всё это в 1 список телефонов
    phones = [list(r)[:len(r)-1:] for r in operators]
    phones = list(itertools.chain.from_iterable(phones))
    # Найдём нужный тапл, если считать, что в каждом тапле только 2 телефона и 1 опретор, то будет работать
    return operators[bisect_left(phones, number)//2][2]


# print(get_operator_bisect(operators_data, '7333333333'))
# print(get_operator(operators_data, '7333333333'))
assert get_operator(operators_data, '7111222222') == 'operator-1'
assert get_operator(operators_data, '7333333333') == 'operator-2'
assert get_operator_bisect(operators_data, '7111222222') == 'operator-1'
assert get_operator_bisect(operators_data, '7333333333') == 'operator-2'