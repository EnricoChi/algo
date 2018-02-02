# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

while True:
    num = input('Введите натуральное число: ')
    num_list = [int(n) for n in num]

    if num_list:
        even = 0
        odd = 0
        for n in num_list:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
        print('Чётных {}\nНечётных {}'.format(even, odd))
