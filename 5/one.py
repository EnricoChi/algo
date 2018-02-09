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

from collections import Counter
from random import randint


def search_lst(lst):
    result_lst = []
    for _ in range(len(lst)):
        # Будем брать/удалять последний элемент
        current = lst.pop()  # O(1)
        # И проверять, бывает ли он ещё в это списке
        if current in lst:  # O(n) list
            # Если бывает, то запишем в результат
            result_lst.append(current)  # O(1)
    return set(result_lst)


'''
    Результат почти в 2 раза быстрее, чем в прошлый раз!
    > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_lst" "search_lst([randint(0, 100000) for i in range(100000)])"
    1 loops, best of 1: 58.2 sec per loop
    
    А так всёравно грустно, хоть и не так как раньше. Можно это ещё больше оптимизировать?
    > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import search_lst" "search_lst([randint(0, 200000) for i in range(200000)])"
    1 loops, best of 1: 234 sec per loop
'''


def counter_lst(lst):
    result_lst = []
    search = Counter(lst)
    for k, v in search.items():
        if v > 1:
            result_lst.append(k)
    return result_lst

'''
    Анрил
    > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import counter_lst" "counter_lst([randint(0, 1000000) for i in range(1000000)])"
    1 loops, best of 1: 1.81 sec per loop
    
    > python -m timeit -n 1 -r 1 -s "from random import randint" "from one import counter_lst" "counter_lst([randint(0, 10000000) for i in range(10000000)])" 
    1 loops, best of 1: 21 sec per loop
'''


# test_lst = [randint(0, 1000000) for i in range(1000000)]
# print(counter_lst(test_lst))

test_lst = [9, 4, 6, 4, 10, 0, 4, 0, 6, 8]
# assert search_lst(test_lst) == {0, 4, 6}
assert counter_lst(test_lst) == [4, 6, 0]

