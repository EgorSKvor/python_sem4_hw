# # Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# # Пример:
# # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
# rand = random.randint(0, 100)
k = int(input('Enter num --> '))
x = 1
formula = 0
# for i in range(k):
#     # formula = rand*(x**k) + rand*(x**(k-1)) + rand*(x**(k-2))
#     formula += rand*(x**k)
#     k -= 1
with open('file.txt', 'w') as data:  # очистка файла перед записью
    pass
while m := k + 1 != 0:
    formula = random.randint(0, 100)*(x**k)
    with open('file.txt', 'a') as data:
        if k != 0:
            data.write(f'{formula} + ')
        else:
            data.write(f'{formula}')
    k -= 1
