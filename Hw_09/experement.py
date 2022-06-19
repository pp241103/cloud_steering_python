#!/usr/bin/env python3

'''
test_1_1 - test_1_4: Problem 9 Pythagorean triplet.   Good: test_1_4
test_2_1           : Problem 6 Sum square difference. Good: test_2_1
try_3_1            : Problem 48 Self powers.          Good: try_3_1
'''
# -------------------Problem 9 Pythagorean triplet--------------------

# a, b, c = 0, 0, 0

def try_1_1():
  for a in range(1, 1001):
    for b in range(1, 1001):
      for c in range(1, 1001):
        if a + b + c == 1000:
          if a**2 + b**2 == c**2:
            return [a, b, c]

def try_1_2():
  for a in range(1, 1000):
    for b in range(1, 1000):
      c = 1000 - b - a
      if a**2 + b**2 == c**2:
        return [a, b, c]

def test_1_1():
  r = []
  for x in [1,2,3]:
    for y in [3,1,4]:
      if x!=y:
        r.append((x,y))
  
  r1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
  return r1 == r

def test_1_2():
  r=[]
  for a in range(1, 1000):
    for b in range(1, 1000):
      c = 1000 - b - a
      if a**2 + b**2 == c**2:
        r = [a,b,c]
        break
    else:
      continue
    break
  print(r)

def test_1_3():
  return [[a, b, c] for a in range(1, 1000) \
                    for b in range(1, 1000) \
                    for c in range(1, 1000) \
                    if a + b + c == 1000 \
                    if a**2 + b**2 == c**2]

def test_1_4():
  '''
  HELP
  ----
  [(i, j) for i in range(1,1000) \
          for j in range(1,1000) \
          if (1000 - i - j)**2 -i**2-j**2 == 0]
  [(200, 375), (375, 200)]
  '''
  return [(i, j, 1000 - i - j) for i in range(1,1000) \
                               for j in range(1,1000) \
                               if (1000 - i - j)**2 -i**2-j**2 == 0]
  
# print(test_1_1())
# test_1_2()
# print(test_1_3())
# print(test_1_4()) # <-- This is good

# --------------------------End of Problem 9--------------------------

# ------------------Problem 6 Sum square difference-------------------

def try_2_1(n):
  sum_of_sq = sum([x**2 for x in range(1, n + 1)])
  sq_of_sum = sum([x for x in range(1, n + 1)]) ** 2
  diff = sq_of_sum - sum_of_sq
  return { "sum_of_sq": sum_of_sq, \
           "sq_of_sum": sq_of_sum , \
           "diff": diff}

def test_2_1():
  return (sum([x for x in range(1, 100 + 1)]) ** 2) - \
         (sum([x**2 for x in range(1, 100 + 1)]))



# print(try_2_1(100))
# print(test_2_1()) # <-- This is good

# ---------------End of Problem 6 Sum square difference---------------

# -----------------------Problem 48 Self powers-----------------------

def try_3_1(n): # <-- good
  return str(sum([x**x for x in range(1, n + 1)]))[-10:]

# This is not my function
def try_3_2():
  def modpow(b, e, m):
    r = 1
    while e > 0:
      if e & 1:
        r = (r * b) % m
      b = (b * b) % m
      e = e >> 1
    return r
  def powersum(n, m):
    s = 0
    for i in range(1, n + 1):
      s+= modpow(i, i, m)
      s%= m
    return s
  
  print(powersum(1000, 10000000000))

# THE END RESULT
# print("This is my", try_3_1(1000))

# NOT MY SOLUTION
# print("This is not my:", try_3_2())

# -------------------End of Problem 48 Self powers--------------------
# -----------------Problem 40 Champernowne's constant-----------------
import math

def try_4_1(n):
  s, i = "", 0
  while len(s) < n + 1:
    s += str(i)
    i += 1
  return s

print(math.prod([int(try_4_1(1_000_000)[10 ** i]) for i in range(7)]))
# -------------End of Problem 40 Champernowne's constant--------------
