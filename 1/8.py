# 8. Определить, является ли год, который ввел пользователем, високосным или не високосным.


# Если не делится на 4 без остатка
#   обычный
# Иначе если делится на 100,
#   столетие.
#       Если делится на 400,
#           високосный.
#       Иначе обычный.

while True:
    year = int(input('Введите год: '))

    if year % 4 != 0:
        print('{} обычный год\n'.format(year))
    elif year % 100 == 0:
        if year % 400 == 0:
            print('{} високосный год\n'.format(year))
        else:
            print('{} обычный год\n'.format(year))
    else:
        print('{} високосный год\n'.format(year))
