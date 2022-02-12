import math

a, b, c = (int(input()) for _ in range(3))

D = b ^ 2 + 4 * a * c
if D > 0:
    x1 = (b * (-1) + math.sqrt(D)) / 2 * a
    x2 = (b * (-1) - math.sqrt(D)) / 2 * a
    print('Первый корень = ', x1)
    print('Второй корень = ', x2)

elif D == 0:
    x = b * (-1) / 2 * a
    print('Корень = ', x)

else:
    print('Корней нет')
