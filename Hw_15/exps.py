#!/usr/bin/env python3
# /home/peter/Cloud_steering/Labs/Python/Done/Hw_15/experiments.py

from ipaddress import *
from pprint import pprint as pp
import Router as r
r1 = r.Router()
print("Created router r1")
r1.add_interface("192.168.5.14/24")
print("Added interface 192.168.5.14/24")
r1.add_route("192.168.5.1", "172.16.0.0/16")
print("Added router ip 192.168.5.1 to network 172.16.0.0/16")
# r1.add_route("192.168.8.1", "172.24.0.0/16")
r1.add_route("172.16.8.1" , "172.24.0.0/16")
print("Added router ip 172.16.8.1 to network 172.24.0.0/16")
print("Now we have this sate of r1")
pp(r1._ifs)
pp(r1._routes)
r1.del_interface("192.168.5.14/24")
print("Delete interface 192.168.5.14/24")
print("Now we have this sate of r1")
pp(r1._ifs)
pp(r1._routes)
r1.del_route("172.16.0.0/16")
print("Delete the route to network 172.16.0.0/16")
print("Now we have this sate of r1")
r1.display()
