#!/usr/bin/env python3

import sys

# Get list of types and return a list of its all unique methods
def uniq(in_list):
  uniq = []
  for i in in_list:
    uniq += dir(eval(i))
  uniq = list(set(uniq))
  uniq.sort()
  return uniq

# Gets list of methods and types. Forms csv-sytax output of presence 
# or absence the method in type.
def table(methods, types):
  output = "Methods \\ Types"
  for i in types:
    output += ",{}".format(i)
  for i in methods:
    output += "\n{}".format(i)
    for j in types:
      if i in dir(eval(j)):
        output += ",yes"
      else:
        output += ",no"

  return output

types = sys.argv[1:]
methods = uniq(types)
print(table(methods,types))