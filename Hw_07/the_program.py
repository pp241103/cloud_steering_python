#!/usr/bin/env python3

s = ""
l = []
sh = []
sh_u = []

with open("/etc/passwd") as fin:
  s = fin.read()

l = s.strip().split("\n")

for i in l:
  sh.append(i.split(":")[-1])

sh_u = list(set(sh))
sh_u.sort()

for i in sh_u:
  print(i, "-", s.count(i), end = " ; ")