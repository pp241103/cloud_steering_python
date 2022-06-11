#!/usr/bin/env python3

import pprint

# Напишите программу, которая читает данные из файлов                                                          
# /etc/passwd и /etc/group на вашей системе и выводит                                                          
# следующую информацию в файл output.txt:                                                                      
# 1. Количество пользователей, использующих все имеющиеся                                                      
# интерпретаторы-оболочки.                                                                                     
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)

def make_dict(file, col1, col2):
  d = dict()
  key = col1 - 1
  val = col2 - 1
  l = file.strip().split("\n")
  for i in l:
    d[i.split(":")[key]] = i.split(":")[val]
  return d

def g_f_u(g_u, gid_g, passwd):
  g_f_u = g_u.copy()
  for i in passwd.strip().split("\n"):
    u_name = i.split(":")[0]
    gid = i.split(":")[3]
    g_name = gid_g[gid]
    if u_name not in g_u[g_name]:
      if g_f_u[g_name] == "":
        g_f_u[g_name] += u_name
      else:
        g_f_u[g_name] += "," + u_name
  return g_f_u

def g_f_uid(g_f_u, u_uid):
  g_f_uid = g_f_u.copy()
  for key in g_f_u:
    tl = g_f_u[key].split(",")
    tl1 = []
    for u_name in tl:
      if u_name != "":
        tl1.append(u_uid[u_name])
    g_f_uid[key] = ",".join(tl1)
  return g_f_uid

def calc_shells(u_s):
  shells = {}
  for sh in u_s.values():
    if sh not in shells:
      shells[sh] = 1
    else:
      shells[sh] += 1
  return shells

passwd = ""
group = ""

with open("/etc/passwd") as fin:
  for line in fin:
    if not line.startswith("#"):
      passwd += line
with open("/etc/group") as fin:
  for line in fin:
    if not line.startswith("#"):
      group += line

u_uid = make_dict(passwd, 1, 3)
u_s = make_dict(passwd, 1, 7)
g_u = make_dict(group, 1, 4)
gid_g = make_dict(group, 3, 1)
g_f_u = g_f_u(g_u, gid_g, passwd)
g_f_uid = g_f_uid(g_f_u, u_uid)
d_shells = calc_shells(u_s)

shells = ""
for key, val in d_shells.items():
  shells += key + " - " + str(val) + " ; "

group_uids = ""
for key, val in g_f_uid.items():
  group_uids += key + ":" + val + ", "

with open("./output.txt", "w") as ouf:
  ouf.write(shells + "\n")

with open("./output.txt", "a") as ouf:
  ouf.write(group_uids + "\n")

print("The information is written to a file (./output.txt)")