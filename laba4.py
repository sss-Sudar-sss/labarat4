print("Задание 1: числа между А и В по убыванию")
while True:
    try:
        A=int(input("Введите целое число А: "))
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте еще раз.")
