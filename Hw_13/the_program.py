#!/usr/bin/env python3

"""
Напишите функцию, которая переводит значения показаний
температуры из Цельсия в Фаренгейт и наоборот.
"""

# example:  convert_from_unit(1, "C") -> 33.8°F
def convert_from_unit(value = 1, unit = "c"):
  # From C to F
  if unit.strip().rstrip().lower() == "c":
    return round(value * 9/5 + 32, 1)
  # From F to c
  elif unit.strip().rstrip().lower() == "f":
    return round((value - 32) * 5/9, 1)
  else:
    print("c - for Celsius\nf - for Fahrenheit")

print("1 C =", convert_from_unit(1), "Fahrenheit")
print("0 F =", convert_from_unit(0, "F"), "Celsius")
print("10 F =", convert_from_unit(10, "f"), "Celsius")
print("90 C =", convert_from_unit(90, "c"), "Fahrenheit")
print("90 C =", convert_from_unit(90, "C"), "Fahrenheit")