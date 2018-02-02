# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

abc = 'abcdefghijklmnopqrstuvwxyz'

while True:
    letters = input('Две буквы через запятую - a,f: ').split(',')
    lettetr_operation = 'Буква {} имеет позицию {}, буква {} имеет позицию {}, в промежутке {} букв'.format(
        letters[0],
        abc.find(letters[0]),  # Ищем индекс символа в строке
        letters[1],
        abc.find(letters[1]),
        len(abc[abc.find(letters[0]):abc.find(letters[1])]) - 1)  # Считаем длинну среза минус еденица, чтобы исключить первый символ

    print(lettetr_operation)
