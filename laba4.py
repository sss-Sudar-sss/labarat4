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
num=[]
for i in range(B-1,A,-1):
    num.append(i)
print("Числа между A и B (не включая границы), по убыванию:")
print(*num)
N=len(num)
print("Количество чисел N =",N)


#Задание 2

