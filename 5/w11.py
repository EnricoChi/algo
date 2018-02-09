# 11. Вывести какой-либо символ по диагоналям воображаемого квадрата.

a, b = [20, 20]


def figure1(a, b):
    for i in range(a):
        for j in range(a):
            if i == j or i == (a - 1) - j:
                # Пробелы, чтобы хоть как-то относительно было похоже на диагональ квадрата
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print(' ')
    return None


# python -m timeit -n 1 -r 1 -s "from w11 import figure1" "figure1(5000, 5000)"
# 1 loops, best of 1: 43.2 sec per loop

# python -m timeit -n 1 -r 1 -s "from w11 import figure1" "figure1(10000, 10000)"
# 1 loops, best of 1: 172 sec per loop


# Думаю что математического обьяснения этому не существует, и понять это впринципе невозможно.
# Но зато линейная сложность
def figure(a, b):
    result = []
    for i in range(a):
        # абракадабра
        if i < b // 2:
            result.append('{:.<{}}{:.>{}}'.format('.' * i + '\\', b // 2, '/' + '.' * i, b // 2))
        else:
            i += 1
            result.append('{:.<{}}{:.>{}}'.format('.' * (b - i) + '/', b // 2, '\\' + '.' * (b - i), b // 2))
    return result


test = figure(a, b)
for i in test:
    print(i)


'''
    Если принтить
'''
# python -m timeit -n 1 -r 1 -s "from w11 import figure" "figure(5000, 5000)"
# 1 loops, best of 1: 12.7 sec per loop

# python -m timeit -n 1 -r 1 -s "from w11 import figure" "figure(10000, 10000)"
# 1 loops, best of 1: 42.2 sec per loop

'''
    Если принты поменять на запись в список result
'''
# > python -m timeit -n 1 -r 1 -s "from w11 import figure" "figure(10000, 10000)"
# 1 loops, best of 1: 83.2 msec per loop

# > python -m timeit -n 1 -r 1 -s "from w11 import figure" "figure(20000, 20000)"
# 1 loops, best of 1: 593 msec per loop

# > python -m timeit -n 1 -r 1 -s "from w11 import figure" "figure(100000, 100000)"
# 1 loops, best of 1: 59.1 sec per loop
