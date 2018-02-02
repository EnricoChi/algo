# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

while True:
    nums = input('Введите три числа ~ 1,2,3: ')

    if nums:
        try:
            nums = [int(s) for s in nums.split(',')]
        except ValueError:
            print('Попробуйте снова!\n')
            continue
    else:
        print('Попробуйте снова!\n')
        continue

    try:
        a, b, c = nums
    except ValueError:
        print('Попробуйте снова!\n')
        continue

    if a > b:
        if a > c:
            if b > c:
                print('Среднее {}\n'.format(b))
            else:
                print('Среднее {}\n'.format(c))
        else:
            print('Среднее {}\n'.format(a))
    else:
        if b > c:
            if a > c:
                print('Среднее {}\n'.format(a))
            else:
                print('Среднее {}\n'.format(c))
        else:
            print('Среднее {}\n'.format(b))
