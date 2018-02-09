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

# lst = [randint(0, 100) for i in range(100)]
lst = [9, 4, 6, 4, 10, 0, 4, 0, 6, 8]

# {0, 4, 6, 8, 9, 10}


def search_lst(lst):
    result_lst = []
    for _ in range(len(lst)):
        # Будем брать/удалять последний элемент
        current = lst.pop()  # O(1)
        # И проверять, бывает ли он ещё в это списке
        if current in lst and current not in result_lst:  # O(n) list
            # Если бывает, то запишем в результат
            result_lst.append(current)  # O(1)
    # Развернём, т.к. поиск был с конца
    return result_lst[::-1]


'''
    Результат в 2 раза быстрее, чем в прошлый раз!
    > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_lst" "search_lst([randint(0, 100000) for i in range(100000)])"
    1 loops, best of 1: 40.8 sec per loop
    
    А так всёравно грустно, хоть и не так как раньше. Можно это ещё больше оптимизировать?
    > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_lst" "search_lst([randint(0, 200000) for i in range(200000)])"
    1 loops, best of 1: 174 sec per loop
'''


def search_set(lst):
    result_set = set()
    convert = set(lst)
    print(convert)
    for i in range(len(lst)):
        # Будем брать/удалять последний элемент
        current = lst.pop()  # O(1)
        print(current)
        # И проверять, бывает ли он ещё в это списке
        if current in convert:  # O(1) set
            # Если бывает, то запишем в результат
            result_set.add(current)  # O(1)
    # Развернём, т.к. поиск был с конца
    return result_set


'''
    Результат в 2 раза быстрее, чем в прошлый раз!
    > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_lst" "search_lst([randint(0, 100000) for i in range(100000)])"
    1 loops, best of 1: 40.8 sec per loop

    А так всёравно грустно, хоть и не так как раньше. Можно это ещё больше оптимизировать?
    > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_lst" "search_lst([randint(0, 200000) for i in range(200000)])"
    1 loops, best of 1: 174 sec per loop
'''


# print(search_lst(lst))
# test_lst = [9, 4, 6, 4, 10, 0, 4, 0, 6, 8]
# assert search_set(test_lst) == [4, 0, 6]

