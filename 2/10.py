# 10. Вывести на экран "прямоугольник", образованный из двух видов символов.
# Контур прямоугольника должен состоять из одного символа, а в "заливка" - из другого.

# Обьявляем прямоугольник
rectangle = [6, 16]
a, b = rectangle

# Символы для обёртки и внутренностей
wrapper = '+'
inner = '-'

# А теперь понеслась. Интересно как решить это правильно
for i in range(a):
    if i == 0 or i == a - 1:
        print(wrapper * b)
    else:
        print('{}{}{}'.format(wrapper, inner * (b - 2), wrapper))

print('\n\n')

# Или так?
for i in range(a):
    for j in range(b):
        if i == 0 or i == a - 1:
            print(wrapper, end='')
        else:
            if j == 0 or j == b - 1:
                print(wrapper, end='')
            else:
                print(inner, end='')
    print('')
