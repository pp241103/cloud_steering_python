#!/usr/bin/env python3

# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода в виде строки (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:

# 1. После запуска предлагает пользователю ввести текст.
# 2. В качестве ответа печатает наиболее часто встречающееся в тексте слово
# или несколько таких слов, если имеет место "ничья". Также указывая
# сколько именно раз слово встретилось в тексте. (Игнорируйте заглавные буквы
# при отождествлении слов - то есть считайте слова "Подлодка" и "подлодка"
# одинаковыми, а разные формы слов - разными словами)
# После чего ждет следующего ввода.

# Пример:

# -> собака кот кошка Собака
# 2 - собака

# -> собака кот кошка Собака кот
# 2 - собака
# 2 - кот

target = input("-> ")

dict_words = dict.fromkeys(target.lower().split(), 0)
for i in target.lower().split():
  if i in dict_words:
    dict_words[i] += 1

m = max(dict_words.values())
for i, j in dict_words.items():
  if j == m:
    print(j, "-", i)

# Conclusion:
# -----------
# The interesting thin was found. Whene cilce is over the variables 
# like i or j still in the sortof "namespase" and could be found using
# dir().