#!/usr/bin/env python3

from Employee import Employee
from pickle import dump

mary = Employee("Mary", "2223344", 20_000)

with open("mary_employee_dump.pickle", "wb") as ouf:
  dump(mary, ouf)
