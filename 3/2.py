# Вывести неповторяющиеся элементы переданного списка.

from random import randint

lst = [randint(1, 100) for i in range(500)]
unic_lst = []


def search(lst, unic_lst):
    # Базовый случай. Если списка нет, то конец рекурсии
    if lst:
        # Берём первый элемент
        num = lst[0]
        # Считаем сколько раз он повторяется в списке
        i = lst.count(num)
        # Если больше одного раза
        if i > 1:
            # Циклом удаляем его столько раз сколько он встречается
            for item in range(i):
                lst.remove(num)
        # Если только одно вхождение, то добавляем его в список уникальных элементов
        else:
            unic_lst.append(num)
            # И всёравно удаляем из первого списка, чтобы рано или поздно возбудить базовый случай
            lst.remove(num)
        return search(lst, unic_lst)
    else:
        return unic_lst


print(lst)
print(search(lst, unic_lst))
