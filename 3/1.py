# Реализовать бинарный поиск с помощью рекурсии.
from random import randint

num = randint(0, 1000)

# Сгенерим непредвзятый список
arr = [(i*2)-5 for i in range(1000)]
start = 0
end = len(arr) - 1


def search(num, arr, start, end):
    # Определим длинну
    middle = (start + end) // 2
    # Это базовый случай?
    if end < start:
        return False
    else:
        # Или это? Или оба?
        if num == arr[middle]:
            return middle
        # Шаг
        elif num > arr[middle]:
            start = middle + 1
            return search(num, arr, start, end)
        else:
            end = middle - 1
            return search(num, arr, start, end)


result = search(num, arr, start, end)
print('Число - {} индекс - {}'.format(num, result))
