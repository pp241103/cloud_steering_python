#!/usr/bin/env python3

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def fun():
    n = input("-> ")
    if n.isdigit():
        if int(n) % 2 == 0:
            print(int(int(n) / 2))
            fun()
        else:
            print(int(n) * 3 + 1)
            fun()
    elif n == "cancel":
        print("Bye!")
    elif is_float(n):
        print("Введите целое число")
        fun()
    else:
        print("Не удалось преобразовать введенный текст в число.")
        fun()

fun()
