#!/usr/bin/env python3
# /home/peter/Cloud_steering/Labs/Python/Done/Hw_15/experiments.py

from ipaddress import *
from pprint import pprint as pp
import Router as r
r1 = r.Router()
r1.add_interface("192.168.5.14/24")
r1.add_route("192.168.5.1", "172.16.0.0/16")
# r1.add_route("192.168.8.1", "172.24.0.0/16")
r1.add_route("172.16.8.1" , "172.24.0.0/16")
r1.display()
r1.del_interface("192.168.5.14/24")
r1.display()
r1.del_route("172.16.0.0/16")
r1.display()
