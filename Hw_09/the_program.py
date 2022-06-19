#!/usr/bin/env python3

import math

# -------------------Problem 9 Pythagorean triplet--------------------
print("9:", [(i, j, 1000 - i - j) for i in range(1,1000) for j in range(1,1000) if (1000 - i - j)**2 -i**2 -j**2 == 0])

# ------------------Problem 6 Sum square difference-------------------
print("6:", (sum([x for x in range(1, 100 + 1)]) ** 2) - (sum([x**2 for x in range(1, 100 + 1)])))

# -----------------------Problem 48 Self powers-----------------------
print("48:", str(sum([x**x for x in range(1, 1000 + 1)]))[-10:])

# -------------End of Problem 40 Champernowne's constant--------------
def try_4_1(n):
  s, i = "", 0
  while len(s) < n + 1:
    s += str(i)
    i += 1
  return s

print("40:", \
      math.prod([int(try_4_1(1_000_000)[10 ** i]) for i in range(7)]))
