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


from random import randint
from collections import Counter


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


def search_set(lst):
    result_set = set()
    set1 = set()
    for _ in range(len(lst)):
        current = lst.pop()
        if current not in set1:
            set1.add(current)
        else:
            result_set.add(current)
    return result_set


# test_lst = [9, 4, 6, 4, 10, 0, 4, 0, 6, 8]
test_lst = [65, 65, 44, 46, 50, 10, 57, 54, 80, 82, 30, 44, 23, 68, 28, 45, 32, 84, 53, 54, 49, 37, 66, 93, 83, 7, 96, 20, 83, 29, 44, 24, 63, 70, 78, 31, 20, 93, 42, 15, 37, 0, 29, 14, 75, 61, 95, 66, 1, 17, 30, 86, 35, 64, 88, 18, 3, 40, 55, 59, 5, 80, 39, 79, 70, 17, 33, 63, 24, 69, 12, 47, 84, 58, 100, 58, 19, 3, 41, 75, 73, 17, 32, 84, 95, 60, 77, 46, 31, 41, 27, 62, 28, 81, 34, 58, 100, 36, 80, 61]  #[randint(0, 100) for i in range(100)]
# print(test_lst)
# print(search_set(test_lst))


assert search_set(test_lst) == {3, 17, 20, 24, 28, 29, 30, 31, 32, 37, 41, 44, 46, 54, 58, 61, 63, 65, 66, 70, 75, 80, 83, 84, 93, 95, 100}

# assert counter_lst(test_lst) == [4, 6, 0]

