# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

abc = 'abcdefghijklmnopqrstuvwxyz'

while True:

    try:
        letter_num = int(input('Номер буквы: '))
    except ValueError:
        print('\nВы ничего не ввели или ввели неверное значение')
    else:
        if letter_num:
            if letter_num <= len(abc):
                print('Буква по номером {} - {}'.format(letter_num, abc[letter_num - 1]))
            else:
                print('Не больше {}, попробуйте снова'.format(len(abc)))

