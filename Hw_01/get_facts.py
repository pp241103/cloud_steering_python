#!/usr/bin/env python3

# List of uniq methods of <class 'int'> <class 'str'> <class 'bool'>
uniq = list(set(dir(int) + dir(str) + dir(bool)))
uniq.sort()

print("Methods,int,str,bool")

for i in uniq:
  print(i, end = ",")
  if i in dir(int):
    print("yes,", end = "")
  else:
    print("no,", end = "")
  if i in dir(str):
    print("yes,", end = "")
  else:
    print("no,", end = "")
  if i in dir(bool):
    print("yes")
  else:
    print("no")