# Задание 1.
# Отсортировать список [('str1', 'str2'), ('str4', 'str2'), ('str2', 'str3')]
# по возрастанию второй колонки и по убыванию первой колонки.
# В результате должно быть [('str4', 'str2'), ('str1', str2'), ('str2', 'str3')].

lst = [('str1', 'str2'), ('str4', 'str2'), ('str2', 'str3')]


def lst_sorting(lst):
    # по убыванию первой колонки (в минимальном приоретете)
    col1 = sorted(lst, key=lambda i: i[0], reverse=True)
    # по возрастанию второй колонки
    result = sorted(col1, key=lambda i: i[1])
    return result


assert lst_sorting(lst) == [('str4', 'str2'), ('str1', 'str2'), ('str2', 'str3')]
