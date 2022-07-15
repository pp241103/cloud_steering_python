#!/usr/bin/env python3

import ipaddress as ipad
from pprint import pprint as pp

class Router:
  """
  A class used to represent a Router

  Attributes:
  -----------
  routes : dict
    { <next_hop_address> : <destination_network> , and so on... }
    { <ipaddress.IPv4Address> : <ipaddress.IPv4Network> , and so on... }
  ifs : list
    [ <ip_address/CIDR>, <ipaddress.IPv4Interface>, ... ]
    [ <ipaddress.IPv4Interface>, <ipaddress.IPv4Interface>, ... ]
  Methods:
  --------
  add_interface(interface)
    Add an ipaddress.IPv4Interface to `ifs` list
  """
  def __init__(self):
    self._ifs = []
    self._routes = {}
  # Router Interfaces methods
  def add_interface(self, interface):
    """
    Add interface to a Router

    Parameters:
    ----------
    interface : ipaddress.IPv4Interface
    """
    if type(ipad.ip_interface(interface)) == ipad.IPv4Interface:
      interface = ipad.ip_interface(interface)
      self._ifs.append(interface)
      self._routes[interface.ip] = interface.network
  def del_interface(self, interface):
    """
    Delete interface from interfaces list
    and
    Delete corresponding route
    """
    if type(ipad.ip_interface(interface)) == ipad.IPv4Interface:
      interface = ipad.ip_interface(interface)
      if interface in self._ifs:
        # Delete corresponding the route
        self._routes.pop(interface.ip)
        # Delete the interface
        while interface in self._ifs:
          self._ifs.remove(interface)
  def pr_interfaces(self):
    """
    Print info about interfaces
    """
    print("My interfaces:")
    pp(self._ifs)
  # Router routes methods
  def add_route(self, next_hop, network):
    """
    Parameters:
    -----------
    next_hop : ipaddress.IPv4Address
    network : ipaddress.IPv4Network
    """
    found = False
    if type(ipad.ip_address(next_hop)) == ipad.IPv4Address and\
       type(ipad.ip_network(network))  == ipad.IPv4Network:
      next_hop = ipad.ip_address(next_hop)
      network  = ipad.ip_network(network)
      for nw in self._routes.values():
        if next_hop in nw:
          # print("we have connection to network where netx_hop ip address is")
          found = True
          break
      if found:
        self._routes[next_hop] = network
        pass
      else:
        raise ipad.AddressValueError()
  def del_route(self, network):
    """
    Delete route from routes dict
    """
    if type(ipad.ip_network(network))  == ipad.IPv4Network:
      network  = ipad.ip_network(network)
      if network in self._routes.values():
        ips = []
        for k, v in self._routes.items():
          if network == v:
            ips.append(k)
        for i in ips:
          self._routes.pop(i)
  def pr_routes(self):
    """
    Print info about routes
    """
    print("These are my routes:")
    pp(self._routes)
  # Other methods
  def display(self):
    print("ifs:")
    pp(self._ifs)
    print("routes") 
    pp(self._routes)
