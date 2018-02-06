# Задача 1.
#
# Для каждого числа входного массива чисел очень большого размера (100000+ чисел) вывести,
# встречалось такое число ранее среди предшествующих ему элементов массива или нет.

# Сделать три реализации с использованием разных описанных на занятиях контейнеров
# (реализация со списком, реализация со словарем и реализация со множеством в качестве
# контейнера для уже встречавшихся чисел). Сравнить их производительность на массивах большого размера.
#
# Для замера производительности генерировать входной массив с помощью
# input_array = [ random.randint (0, 1000000) for i in range(100000) ]
# (при желании можно увеличить размер массива и диапазон чисел в 10/100 раз).
# При замере производительности рекомендуется не печатать сообщения в консоль.

"""
    При замере производительности разница не существенна. Но множества быстрее всех, да.
    По второму кругу, словарь почему-то отработал быстрее чем список.
    А может просто кривокод.
"""

from random import randint

lst = [randint(0, 100) for i in range(100)]


def search_lst(lst):
    result_lst = []
    # Мы же будем искать предшевствующие элементы, поэтому логично начать искать их с конца списка
    invert_lst = lst[::-1]
    # Будет циклить по индексу, а не по значению
    for i in range(len(invert_lst)):
        # Элемент с текущим индексом
        current = invert_lst[i]
        # Будем двигаться вправо по списку, исключая текущий элемент
        # и смотреть, чтобы его не было в результирующем
        if current in invert_lst[i + 1:] and current not in result_lst:
            result_lst.append(invert_lst[i])
    return result_lst[::-1]


# print(search_lst(lst))


# > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_lst" "search_lst([randint(0, 100000) for i in range(100000)])"
# 1 loops, best of 1: 94.3 sec per loop

# > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_lst" "search_lst([randint(0, 100000) for i in range(100000)])"
# 1 loops, best of 1: 113.3 sec per loop

def search_dict(lst):
    result_dict = {}
    invert_lst = lst[::-1]
    for i in range(len(invert_lst)):
        current = invert_lst[i]
        # Будем проверять среди значений дикта
        if current in invert_lst[i + 1:] and current not in result_dict.values():
            # Пишем пару - "значение: его индекс"
            result_dict[current] = i
    return result_dict


# print(search_dict(lst))


# > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_dict" "search_dict([randint(0, 100000) for i in range(100000)])"
# 1 loops, best of 1: 98.9 sec per loop

# > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_dict" "search_dict([randint(0, 100000) for i in range(100000)])"
# 1 loops, best of 1: 110 sec per loop

def search_set(lst):
    result_set = set()
    invert_lst = lst[::-1]
    for i in range(len(invert_lst)):
        current = invert_lst[i]
        # Тоже самое, только на одну проверку меньше, т.к. set содержит только уникальные значения
        if current in invert_lst[i + 1:]:
            result_set.add(current)
    return result_set


# print(search_set(lst))

# > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_set" "search_set([randint(0, 100000) for i in range(100000)])"
# 1 loops, best of 1: 85.8 sec per loop

# > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_set" "search_set([randint(0, 100000) for i in range(100000)])"
# 1 loops, best of 1: 88.2 sec per loop

