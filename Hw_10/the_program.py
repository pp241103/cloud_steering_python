#!/usr/bin/env python3

def coll(n):
  st_cnt = 0
  while n != 1:
    if n % 2 == 0:
      n /= 2
      st_cnt += 1
    elif n % 2 == 1:
      n = n*3 + 1
      st_cnt += 1
    else:
      print("Enter an integer pls")
      return None
  return st_cnt

print(coll(12))
print(coll(112))
print(coll(1_000_000_000))
print(coll(112.5))
