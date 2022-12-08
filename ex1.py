# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141
# Ввод: 0.01
#     Вывод: 3.14

import math
p = math.pi

num = input('Enter num --> ')
splt = num.split('.')
acc = len(splt[1])
print(round(p, acc))
