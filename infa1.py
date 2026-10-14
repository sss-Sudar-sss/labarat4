import math
print("Задача 1")
print("Введите x:")
x=float(input())
print("Введите y:")
y=float(input())
if x==0:
    print('Ошибка! х не может быть равен нулю.')
elif y<0:
    print('Ошибка! y не может быть меньше нуля.')
else:
    if x + math.sqrt(y)/(x**2)<=0:
        print('Ошибка! Аргумент логарифма не может быть равен или меньше нуля.')
    else:
        z=math.log2(x + math.sqrt(y)/(x**2))
        print('Ваш ответ:', z)



print("Задача 2")
print("Введите x:")
x = float(input())
a = 1.5
if x <1:
    y = 1.5 * (math.cos(x)**2)
elif x == 1:
    y=1.8 * a * x
elif x>1:
    y=((x - 2)**2) + a
print("Ваш ответ:", y)