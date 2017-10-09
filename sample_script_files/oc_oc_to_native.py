### Translate OpenConfig to native  configuration

from napalm_base import get_network_driver
import napalm_yang
from pprint import pprint
from json import dumps
junos_driver = get_network_driver('junos')

"""
junos_device = {
     'hostname': '192.168.0.30',
     'username': 'mab',
     'password': 'mab123',
 }
"""

device = junos_driver(hostname='192.168.0.30',username='mab',password='mab123', optional_args={'profile':["junos"]})
#device.open()
running_config = napalm_yang.base.Root()
running_config.add_model(napalm_yang.models.openconfig_interfaces())
#type(running_config)

oc_config = {
     "interfaces": {
         "interface": {
             "ge-0/0/0": {
                 "name": "ge-0/0/0", 
                 "subinterfaces": {
                     "subinterface": {
                         "0": {
                             "index": "0", 
                             "ipv4": {
                                 "config": {
                                     "enabled": True
                                 }, 
                                 "addresses": {
                                     "address": {
                                         "192.168.0.35": {
                                             "ip": "192.168.0.35", 
                                             "config": {
                                                 "ip": "192.168.0.35", 
                                                 "prefix-length": 24
                                             }
                                         }
                                     }
                                 }
                             }, 
                             "config": {
                                 "enabled": True, 
                                 "name": "0"
                             }
                         }
                     }
                 }, 
                 "routed-vlan": {
                     "ipv4": {
                         "config": {
                             "enabled": False
                         }
                     }
                 }, 
                 "config": {
                     "type": "ethernetCsmacd", 
                     "enabled": True, 
                     "name": "ge-0/0/0"
                 }
             }
         }
     }
 }


running_config.load_dict(oc_config)

print(running_config.translate_config(device.profile))