# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

def func():
    # 1 способ решения задачи

    l = list(map(int, input('Введите список:\n').split(',')))
    min = int(input('Минимальное значение: '))
    max = int(input('Максимальное значение: '))

    l2 = [i for i in range(len(l)) if min <= l[i] <= max]
    print(l2)
    
func() # Запуск 1 варианта решения
