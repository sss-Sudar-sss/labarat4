import math
#Задание 1

print("Задание 1: числа между А и В по убыванию")
while True:
    try:
        A=int(input("Введите целое число А: "))
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте еще раз.")
while True:
    try:
        B=int(input("Введите целое число B: "))
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте еще раз.")
        continue
    if A < B:
        break
    print("Ошибка: должно выполняться условие А < B. Повторите ввод еще раз.")
if A+1 == B:
    print("Между A и В нет целых чисел")
    print("Количество N чисел между ними:")
    print("N=0")
else:
    num=[]
    for i in range(B-1,A,-1):
        num.append(i)
    print("Числа между A и B (не включая границы), по убыванию:")
    print(*num)
    N=len(num)
    print("Количество чисел N =",N)
print()

#Задание 2
print("Задание 2: табулирование функции z(x)")

while True:
    try:
        X0 = float(input("Введите X0 (начало отрезка): ").replace(",", "."))
        break
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте еще раз.")
while True:
    try:
        X1 = float(input("Введите X1 (конец отрезка): ").replace(",", "."))

    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте еще раз.")
    if X0 < X1:
        break
    print("Ошибка: требуется X0 < X1. Повторите ввод еще раз.")

while True:
    try:
        dX = float(input("Введите шаг dX: ").replace(",", "."))
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте еще раз.")
        continue
    if X0 < X1 and dX > 0:
        break
    print("Ошибка: требуется X0 < X1 и dX > 0. Повторите ввод еще раз.")

step=int(round((X1-X0) / dX))
for i in range(step+1):
    x = X0 + i * dX
    if x < 0:
        z=x**2
    elif 0 < x <=1:
        z=math.sin(x)
    else:
        z=math.cos(x)
    print("x =",x,"   z=",z)
print()



#Задание3
print("Задание 3: Числа от A до B (включая границы)")
while True:
    try:
        A=int(input("Введите целое число А: "))
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте еще раз.")
while True:
    try:
        B=int(input("Введите целое число B: "))
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте еще раз.")
        continue
    if A != B:
        break
    print("Ошибка: числа A и B не должны совпадать. Повторите ввод еще раз.")
spisok=[]
if A <B:
    print("Числа от A до B (включая границы) в порядке возрастания:")
    count=0
    for x in range(A,B+1):
        spisok.append(x)
        count+=1
    print(*spisok)
else:
    print("Числа от A до B (включая границы) в порядке убывания:")
    count=0
    for x in range(A, B-1, -1):
        spisok.append(x)
        count += 1
    print(*spisok)
print("Количество чисел N =", count)