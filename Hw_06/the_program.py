#!/usr/bin/env python3

# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)

def ispoli(number):
  return (\
    len(number) == 1 or \
    number[::+1][:len(number)//2] == \
    number[::-1][:len(number)//2]\
    )\
    and\
    (\
    len(bin(int(number))[2:]) == 1 or\
    bin(int(number))[2:][::+1][:len(bin(int(number))[2:])//2] == \
    bin(int(number))[2:][::-1][:len(bin(int(number))[2:])//2]\
    )

s = 0

for i in range(1000000):
  if i % 2 == 0:
    continue
  if ispoli(str(i)):
    s += i

print(s)