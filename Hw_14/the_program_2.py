#!/usr/bin/env python3

from pickle import load

with open("mary_employee_dump.pickle", "rb") as inf:
  mary = load(inf)

meggi = mary.__class__("Meggi", "4443322", 1_000_000)
