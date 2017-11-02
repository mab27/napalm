# Lab1

## Overview:
- Simple python files. All information included in the files.

## Getters (show commands):

- get_bgp_config:

```
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_1/configuration/get_bgp_config.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
Raw print: 

{   u'_': {   u'apply_groups': [],
              u'description': u'',
              u'export_policy': u'',
              u'import_policy': u'',
              u'local_address': u'',
              u'local_as': 65070,
              u'multihop_ttl': 0,
              u'multipath': False,
              u'neighbors': {   u'172.16.0.30': {   u'authentication_key': u'',
                                                    u'description': u'vmx1',
                                                    u'export_policy': u'',
                                                    u'import_policy': u'',
                                                    u'local_address': u'',
                                                    u'local_as': 65070,
                                                    u'nhs': False,
                                                    u'prefix_limit': {   },
                                                    u'remote_as': 65030,
                                                    u'route_reflector_client': False},
                                u'172.16.0.40': {   u'authentication_key': u'',
                                                    u'description': u'vmx2',
                                                    u'export_policy': u'',
                                                    u'import_policy': u'',
                                                    u'local_address': u'',
                                                    u'local_as': 65070,
                                                    u'nhs': False,
                                                    u'prefix_limit': {   },
                                                    u'remote_as': 65040,
                                                    u'route_reflector_client': False},
                                u'172.16.0.80': {   u'authentication_key': u'',
                                                    u'description': u'aritsa2',
                                                    u'export_policy': u'',
                                                    u'import_policy': u'',
                                                    u'local_address': u'',
                                                    u'local_as': 65070,
                                                    u'nhs': False,
                                                    u'prefix_limit': {   },
                                                    u'remote_as': 65080,
                                                    u'route_reflector_client': False}},
              u'prefix_limit': {   },
              u'remote_as': 0,
              u'remove_private_as': False,
              u'type': u''}}


JSON dumps print: 

{
    "_": {
        "neighbors": {
            "172.16.0.80": {
                "export_policy": "", 
                "remote_as": 65080, 
                "import_policy": "", 
                "prefix_limit": {}, 
                "local_as": 65070, 
                "nhs": false, 
                "route_reflector_client": false, 
                "local_address": "", 
                "authentication_key": "", 
                "description": "aritsa2"
            }, 
            "172.16.0.40": {
                "export_policy": "", 
                "remote_as": 65040, 
                "import_policy": "", 
                "prefix_limit": {}, 
                "local_as": 65070, 
                "nhs": false, 
                "route_reflector_client": false, 
                "local_address": "", 
                "authentication_key": "", 
                "description": "vmx2"
            }, 
            "172.16.0.30": {
                "export_policy": "", 
                "remote_as": 65030, 
                "import_policy": "", 
                "prefix_limit": {}, 
                "local_as": 65070, 
                "nhs": false, 
                "route_reflector_client": false, 
                "local_address": "", 
                "authentication_key": "", 
                "description": "vmx1"
            }
        }, 
        "export_policy": "", 
        "remote_as": 0, 
        "import_policy": "", 
        "prefix_limit": {}, 
        "local_as": 65070, 
        "multihop_ttl": 0, 
        "apply_groups": [], 
        "local_address": "", 
        "remove_private_as": false, 
        "multipath": false, 
        "type": "", 
        "description": ""
    }
}


Configured remote AS for peer 172.16.0.30 : 65030
------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
Raw print: 

{   'underlay': {   u'apply_groups': [],
                    u'description': u'',
                    u'export_policy': u'bgp-out',
                    u'import_policy': u'bgp-in',
                    u'local_address': u'',
                    u'local_as': 65030,
                    u'multihop_ttl': 0,
                    u'multipath': True,
                    u'neighbors': {   u'172.16.0.40': {   u'authentication_key': u'',
                                                          u'description': u'vmx2',
                                                          u'export_policy': u'',
                                                          u'import_policy': u'',
                                                          u'local_address': u'',
                                                          u'local_as': 0,
                                                          u'nhs': False,
                                                          u'prefix_limit': {   },
                                                          u'remote_as': 65040,
                                                          u'route_reflector_client': False},
                                      u'172.16.0.70': {   u'authentication_key': u'',
                                                          u'description': u'aritsa1',
                                                          u'export_policy': u'',
                                                          u'import_policy': u'',
                                                          u'local_address': u'',
                                                          u'local_as': 0,
                                                          u'nhs': False,
                                                          u'prefix_limit': {   },
                                                          u'remote_as': 65070,
                                                          u'route_reflector_client': False},
                                      u'172.16.0.80': {   u'authentication_key': u'',
                                                          u'description': u'aritsa2',
                                                          u'export_policy': u'',
                                                          u'import_policy': u'',
                                                          u'local_address': u'',
                                                          u'local_as': 0,
                                                          u'nhs': False,
                                                          u'prefix_limit': {   },
                                                          u'remote_as': 65080,
                                                          u'route_reflector_client': False}},
                    u'prefix_limit': {   },
                    u'remote_as': 0,
                    u'remove_private_as': False,
                    u'type': u'external'}}


JSON dumps print: 

{
    "underlay": {
        "neighbors": {
            "172.16.0.80": {
                "export_policy": "", 
                "remote_as": 65080, 
                "route_reflector_client": false, 
                "prefix_limit": {}, 
                "local_as": 0, 
                "nhs": false, 
                "import_policy": "", 
                "local_address": "", 
                "authentication_key": "", 
                "description": "aritsa2"
            }, 
            "172.16.0.70": {
                "export_policy": "", 
                "remote_as": 65070, 
                "route_reflector_client": false, 
                "prefix_limit": {}, 
                "local_as": 0, 
                "nhs": false, 
                "import_policy": "", 
                "local_address": "", 
                "authentication_key": "", 
                "description": "aritsa1"
            }, 
            "172.16.0.40": {
                "export_policy": "", 
                "remote_as": 65040, 
                "route_reflector_client": false, 
                "prefix_limit": {}, 
                "local_as": 0, 
                "nhs": false, 
                "import_policy": "", 
                "local_address": "", 
                "authentication_key": "", 
                "description": "vmx2"
            }
        }, 
        "export_policy": "bgp-out", 
        "remote_as": 0, 
        "description": "", 
        "prefix_limit": {}, 
        "local_as": 65030, 
        "multihop_ttl": 0, 
        "apply_groups": [], 
        "local_address": "", 
        "remove_private_as": false, 
        "multipath": true, 
        "type": "external", 
        "import_policy": "bgp-in"
    }
}


Configured remote AS for peer 172.16.0.70 : 65070
------------------------------------------------------------
------------------------------------------------------------
```
- get_bgp_neighbors:
```
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_1/configuration/get_bgp_neighbors.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------


JSON dumps print: 

{
    "global": {
        "router_id": "70.70.70.71", 
        "peers": {
            "172.16.0.80": {
                "is_enabled": true, 
                "uptime": -2692, 
                "remote_as": 65080, 
                "description": "", 
                "remote_id": "0.0.0.0", 
                "local_as": 65070, 
                "is_up": false, 
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": 0, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": 0
                    }, 
                    "ipv6": {
                        "sent_prefixes": 0, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": 0
                    }
                }
            }, 
            "172.16.0.40": {
                "is_enabled": true, 
                "uptime": -2692, 
                "remote_as": 65040, 
                "description": "", 
                "remote_id": "0.0.0.0", 
                "local_as": 65070, 
                "is_up": false, 
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": 0, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": 0
                    }, 
                    "ipv6": {
                        "sent_prefixes": 0, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": 0
                    }
                }
            }, 
            "172.16.0.30": {
                "is_enabled": true, 
                "uptime": -4424, 
                "remote_as": 65030, 
                "description": "", 
                "remote_id": "30.30.30.31", 
                "local_as": 65070, 
                "is_up": true, 
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": 0, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": 2
                    }, 
                    "ipv6": {
                        "sent_prefixes": 0, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": 0
                    }
                }
            }
        }
    }
}


Uptime for neighbor 172.16.0.30 : -4423


------------------------------------------------------------
Device : vmx1
------------------------------------------------------------


JSON dumps print: 

{
    "global": {
        "router_id": "", 
        "peers": {
            "172.16.0.80": {
                "is_enabled": true, 
                "uptime": 2837, 
                "remote_as": 65080, 
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": -1, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": -1
                    }, 
                    "ipv6": {
                        "sent_prefixes": -1, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": -1
                    }
                }, 
                "remote_id": "", 
                "local_as": 65030, 
                "is_up": false, 
                "description": "aritsa2"
            }, 
            "172.16.0.70": {
                "is_enabled": true, 
                "uptime": 2777, 
                "remote_as": 65070, 
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": 2, 
                        "accepted_prefixes": 0, 
                        "received_prefixes": 0
                    }, 
                    "ipv6": {
                        "sent_prefixes": -1, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": -1
                    }
                }, 
                "remote_id": "70.70.70.71", 
                "local_as": 65030, 
                "is_up": true, 
                "description": "aritsa1"
            }, 
            "172.16.0.40": {
                "is_enabled": true, 
                "uptime": 2837, 
                "remote_as": 65040, 
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": -1, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": -1
                    }, 
                    "ipv6": {
                        "sent_prefixes": -1, 
                        "accepted_prefixes": -1, 
                        "received_prefixes": -1
                    }
                }, 
                "remote_id": "", 
                "local_as": 65030, 
                "is_up": false, 
                "description": "vmx2"
            }
        }
    }
}


Uptime for neighbor 172.16.0.70 : 2778


------------------------------------------------------------
------------------------------------------------------------
```

- get_bgp_neighbors_detail:
```
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_1/configuration/get_bgp_neighbors_details.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
Raw print: 

{   u'default': {   65030: [   {   u'accepted_prefix_count': 2,
                                   u'active_prefix_count': 0,
                                   u'advertised_prefix_count': 0,
                                   u'configured_holdtime': 180,
                                   u'configured_keepalive': 60,
                                   u'connection_state': u'Established',
                                   u'export_policy': u'',
                                   u'flap_count': 0,
                                   u'holdtime': 90,
                                   u'import_policy': u'',
                                   u'input_messages': 116,
                                   u'input_updates': 4,
                                   u'keepalive': 30,
                                   u'last_event': u'RecvKeepAlive',
                                   u'local_address': u'172.16.0.70',
                                   u'local_address_configured': True,
                                   u'local_as': 65070,
                                   u'local_as_prepend': False,
                                   u'local_port': 179,
                                   u'messages_queued_out': 0,
                                   u'multihop': True,
                                   u'multipath': False,
                                   u'output_messages': 104,
                                   u'output_updates': 2,
                                   u'previous_connection_state': u'OpenConfirm',
                                   u'received_prefix_count': 2,
                                   u'remote_address': u'172.16.0.30',
                                   u'remote_as': 65030,
                                   u'remote_port': 50982,
                                   u'remove_private_as': False,
                                   u'router_id': u'30.30.30.31',
                                   u'routing_table': u'default',
                                   u'suppress_4byte_as': False,
                                   u'suppressed_prefix_count': 0,
                                   u'up': True}]}}


JSON dumps print: 

{
    "default": {
        "65030": [
            {
                "accepted_prefix_count": 2, 
                "suppress_4byte_as": false, 
                "local_as_prepend": false, 
                "export_policy": "", 
                "multihop": true, 
                "input_messages": 116, 
                "previous_connection_state": "OpenConfirm", 
                "output_messages": 104, 
                "remove_private_as": false, 
                "multipath": false, 
                "messages_queued_out": 0, 
                "keepalive": 30, 
                "remote_as": 65030, 
                "local_port": 179, 
                "active_prefix_count": 0, 
                "configured_holdtime": 180, 
                "routing_table": "default", 
                "flap_count": 0, 
                "suppressed_prefix_count": 0, 
                "local_address": "172.16.0.70", 
                "input_updates": 4, 
                "configured_keepalive": 60, 
                "router_id": "30.30.30.31", 
                "connection_state": "Established", 
                "local_as": 65070, 
                "remote_address": "172.16.0.30", 
                "advertised_prefix_count": 0, 
                "local_address_configured": true, 
                "import_policy": "", 
                "last_event": "RecvKeepAlive", 
                "remote_port": 50982, 
                "up": true, 
                "output_updates": 2, 
                "received_prefix_count": 2, 
                "holdtime": 90
            }
        ]
    }
}


Connection state for remote AS 65030 : Established


Facing 172.16.0.40  connection is in state :
Facing 172.16.0.80  connection is in state :
Facing 172.16.0.30  connection is in state :Established


------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
Raw print: 

{   u'global': {   65070: [   {   u'accepted_prefix_count': 0,
                                  u'active_prefix_count': 0,
                                  u'advertised_prefix_count': 2,
                                  u'configured_holdtime': 90,
                                  u'configured_keepalive': 30,
                                  u'connection_state': u'Established',
                                  u'export_policy': u'bgp-out',
                                  u'flap_count': 0,
                                  u'holdtime': 90,
                                  u'import_policy': u'bgp-in',
                                  u'input_messages': 95,
                                  u'input_updates': 1,
                                  u'keepalive': 30,
                                  u'last_event': u'RecvKeepAlive',
                                  u'local_address': u'172.16.0.30',
                                  u'local_address_configured': False,
                                  u'local_as': 65030,
                                  u'local_as_prepend': False,
                                  u'local_port': 50982,
                                  u'messages_queued_out': 0,
                                  u'multihop': False,
                                  u'multipath': True,
                                  u'output_messages': 108,
                                  u'output_updates': 1,
                                  u'previous_connection_state': u'OpenConfirm',
                                  u'received_prefix_count': 0,
                                  u'remote_address': u'172.16.0.70',
                                  u'remote_as': 65070,
                                  u'remote_port': 179,
                                  u'remove_private_as': False,
                                  u'router_id': u'70.70.70.71',
                                  u'routing_table': u'global',
                                  u'suppress_4byte_as': False,
                                  u'suppressed_prefix_count': 0,
                                  u'up': True}]}}


JSON dumps print: 

{
    "global": {
        "65070": [
            {
                "suppress_4byte_as": false, 
                "local_as_prepend": false, 
                "connection_state": "Established", 
                "multihop": false, 
                "input_messages": 95, 
                "previous_connection_state": "OpenConfirm", 
                "output_messages": 108, 
                "remove_private_as": false, 
                "multipath": true, 
                "messages_queued_out": 0, 
                "keepalive": 30, 
                "remote_as": 65070, 
                "local_port": 50982, 
                "active_prefix_count": 0, 
                "configured_holdtime": 90, 
                "routing_table": "global", 
                "flap_count": 0, 
                "suppressed_prefix_count": 0, 
                "local_address": "172.16.0.30", 
                "remote_port": 179, 
                "input_updates": 1, 
                "configured_keepalive": 30, 
                "router_id": "70.70.70.71", 
                "export_policy": "bgp-out", 
                "local_as": 65030, 
                "remote_address": "172.16.0.70", 
                "advertised_prefix_count": 2, 
                "local_address_configured": false, 
                "import_policy": "bgp-in", 
                "last_event": "RecvKeepAlive", 
                "accepted_prefix_count": 0, 
                "up": true, 
                "output_updates": 1, 
                "received_prefix_count": 0, 
                "holdtime": 90
            }
        ]
    }
}
Connection state for remote AS 65070 : Established


Facing 172.16.0.40 connection is in state :Active
Facing 172.16.0.80 connection is in state :Active
Facing 172.16.0.70 connection is in state :Established


------------------------------------------------------------
------------------------------------------------------------
```
- get_interfaces:
```
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_1/configuration/get_interfaces.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
Raw print: 

{   u'Ethernet1': {   u'description': u'',
                      u'is_enabled': True,
                      u'is_up': True,
                      u'last_flapped': 1509641899.7547684,
                      u'mac_address': u'00:0C:29:FA:C2:C1',
                      u'speed': 0},
    u'Management1': {   u'description': u'',
                        u'is_enabled': True,
                        u'is_up': True,
                        u'last_flapped': 1509641897.0660176,
                        u'mac_address': u'00:0C:29:69:72:9E',
                        u'speed': 1000}}


JSON dumps print: 

{
    "Management1": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 1509641897.0660188, 
        "is_up": true, 
        "mac_address": "00:0C:29:69:72:9E", 
        "speed": 1000
    }, 
    "Ethernet1": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 1509641899.7547681, 
        "is_up": true, 
        "mac_address": "00:0C:29:FA:C2:C1", 
        "speed": 0
    }
}


Interface Ethernet1 has MAC address : 00:0C:29:FA:C2:C1


------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
Raw print: 

{   '.local.': {   u'description': u'',
                   u'is_enabled': True,
                   u'is_up': True,
                   u'last_flapped': -1.0,
                   u'mac_address': u'Unspecified',
                   u'speed': -1},
    'cbp0': {   u'description': u'',
                u'is_enabled': True,
                u'is_up': True,
                u'last_flapped': -1.0,
                u'mac_address': u'00:05:86:71:E6:11',
                u'speed': -1},
    'demux0': {   u'description': u'',
                  u'is_enabled': True,
                  u'is_up': True,
                  u'last_flapped': -1.0,
                  u'mac_address': u'Unspecified',
                  u'speed': -1},
    'dsc': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'Unspecified',
               u'speed': -1},
    'em1': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:CE',
               u'speed': 1000},
    'em2': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:D8',
               u'speed': 1000},
    'em3': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:E2',
               u'speed': 1000},
    'em4': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:EC',
               u'speed': 1000},
    'em5': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:F6',
               u'speed': 1000},
    'em6': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:00',
               u'speed': 1000},
    'em7': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:0A',
               u'speed': 1000},
    'em8': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:14',
               u'speed': 1000},
    'em9': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:0C:29:88:F0:1E',
               u'speed': 1000},
    'fxp0': {   u'description': u'',
                u'is_enabled': True,
                u'is_up': True,
                u'last_flapped': 2902.0,
                u'mac_address': u'00:0C:29:88:F0:C4',
                u'speed': 1000},
    'ge-0/0/0': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:00',
                    u'speed': 1000},
    'ge-0/0/1': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2855.0,
                    u'mac_address': u'00:05:86:71:E6:01',
                    u'speed': 1000},
    'ge-0/0/2': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:02',
                    u'speed': 1000},
    'ge-0/0/3': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:03',
                    u'speed': 1000},
    'ge-0/0/4': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:04',
                    u'speed': 1000},
    'ge-0/0/5': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:05',
                    u'speed': 1000},
    'ge-0/0/6': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:06',
                    u'speed': 1000},
    'ge-0/0/7': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:07',
                    u'speed': 1000},
    'ge-0/0/8': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:08',
                    u'speed': 1000},
    'ge-0/0/9': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': 2854.0,
                    u'mac_address': u'00:05:86:71:E6:09',
                    u'speed': 1000},
    'gre': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'None',
               u'speed': -1},
    'ipip': {   u'description': u'',
                u'is_enabled': True,
                u'is_up': True,
                u'last_flapped': -1.0,
                u'mac_address': u'None',
                u'speed': -1},
    'irb': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'00:05:86:71:E9:F0',
               u'speed': -1},
    'lc-0/0/0': {   u'description': u'',
                    u'is_enabled': True,
                    u'is_up': True,
                    u'last_flapped': -1.0,
                    u'mac_address': u'Unspecified',
                    u'speed': 800},
    'lo0': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'Unspecified',
               u'speed': -1},
    'lsi': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'Unspecified',
               u'speed': -1},
    'mtun': {   u'description': u'',
                u'is_enabled': True,
                u'is_up': True,
                u'last_flapped': -1.0,
                u'mac_address': u'None',
                u'speed': -1},
    'pfe-0/0/0': {   u'description': u'',
                     u'is_enabled': True,
                     u'is_up': True,
                     u'last_flapped': -1.0,
                     u'mac_address': u'Unspecified',
                     u'speed': 800},
    'pfh-0/0/0': {   u'description': u'',
                     u'is_enabled': True,
                     u'is_up': True,
                     u'last_flapped': -1.0,
                     u'mac_address': u'Unspecified',
                     u'speed': 800},
    'pimd': {   u'description': u'',
                u'is_enabled': True,
                u'is_up': True,
                u'last_flapped': -1.0,
                u'mac_address': u'None',
                u'speed': -1},
    'pime': {   u'description': u'',
                u'is_enabled': True,
                u'is_up': True,
                u'last_flapped': -1.0,
                u'mac_address': u'None',
                u'speed': -1},
    'pip0': {   u'description': u'',
                u'is_enabled': True,
                u'is_up': True,
                u'last_flapped': -1.0,
                u'mac_address': u'00:05:86:71:E9:B0',
                u'speed': -1},
    'pp0': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'Unspecified',
               u'speed': -1},
    'tap': {   u'description': u'',
               u'is_enabled': True,
               u'is_up': True,
               u'last_flapped': -1.0,
               u'mac_address': u'Unspecified',
               u'speed': -1},
    'vtep': {   u'description': u'',
                u'is_enabled': True,
                u'is_up': True,
                u'last_flapped': -1.0,
                u'mac_address': u'Unspecified',
                u'speed': -1}}


JSON dumps print: 

{
    "ge-0/0/7": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2855.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:07", 
        "speed": 1000
    }, 
    "ge-0/0/6": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2855.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:06", 
        "speed": 1000
    }, 
    "ge-0/0/5": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2855.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:05", 
        "speed": 1000
    }, 
    "ge-0/0/4": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2855.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:04", 
        "speed": 1000
    }, 
    "ge-0/0/3": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2855.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:03", 
        "speed": 1000
    }, 
    "ge-0/0/2": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2855.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:02", 
        "speed": 1000
    }, 
    "ge-0/0/1": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2856.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:01", 
        "speed": 1000
    }, 
    "ge-0/0/0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2856.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:00", 
        "speed": 1000
    }, 
    "ge-0/0/9": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2855.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:09", 
        "speed": 1000
    }, 
    "ge-0/0/8": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2855.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:08", 
        "speed": 1000
    }, 
    "tap": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": -1
    }, 
    "demux0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": -1
    }, 
    "pip0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E9:B0", 
        "speed": -1
    }, 
    "pimd": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "None", 
        "speed": -1
    }, 
    "mtun": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "None", 
        "speed": -1
    }, 
    "em5": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:F6", 
        "speed": 1000
    }, 
    "em4": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:EC", 
        "speed": 1000
    }, 
    "em7": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:0A", 
        "speed": 1000
    }, 
    "em6": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:00", 
        "speed": 1000
    }, 
    "em1": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:CE", 
        "speed": 1000
    }, 
    "em3": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:E2", 
        "speed": 1000
    }, 
    "em2": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:D8", 
        "speed": 1000
    }, 
    "lc-0/0/0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": 800
    }, 
    "gre": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "None", 
        "speed": -1
    }, 
    "irb": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E9:F0", 
        "speed": -1
    }, 
    "em9": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:1E", 
        "speed": 1000
    }, 
    "dsc": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": -1
    }, 
    "fxp0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": 2903.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:C4", 
        "speed": 1000
    }, 
    "vtep": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": -1
    }, 
    "cbp0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:05:86:71:E6:11", 
        "speed": -1
    }, 
    "pp0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": -1
    }, 
    "pfh-0/0/0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": 800
    }, 
    "pfe-0/0/0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": 800
    }, 
    "lsi": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": -1
    }, 
    "ipip": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "None", 
        "speed": -1
    }, 
    "em8": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "00:0C:29:88:F0:14", 
        "speed": 1000
    }, 
    "lo0": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": -1
    }, 
    "pime": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "None", 
        "speed": -1
    }, 
    ".local.": {
        "is_enabled": true, 
        "description": "", 
        "last_flapped": -1.0, 
        "is_up": true, 
        "mac_address": "Unspecified", 
        "speed": -1
    }
}


Interface ge-0/0/0 has MAC address : 00:05:86:71:E6:00


------------------------------------------------------------
------------------------------------------------------------
```

- get_interfaces_ip:
```
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_1/configuration/get_interfaces_ip.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
Raw print: 

{   u'Ethernet1': {   u'ipv4': {   u'172.16.0.70': {   u'prefix_length': 24}},
                      u'ipv6': {   }},
    u'Management1': {   u'ipv4': {   u'192.168.0.70': {   u'prefix_length': 24}},
                        u'ipv6': {   }}}


JSON dumps print: 

{
    "Management1": {
        "ipv4": {
            "192.168.0.70": {
                "prefix_length": 24
            }
        }, 
        "ipv6": {}
    }, 
    "Ethernet1": {
        "ipv4": {
            "172.16.0.70": {
                "prefix_length": 24
            }
        }, 
        "ipv6": {}
    }
}
------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
Raw print: 

{   u'em1.0': {   u'ipv4': {   u'172.16.0.1': {   u'prefix_length': 16}},
                  u'ipv6': {   u'fe80::20c:29ff:fe88:f0ce': {   u'prefix_length': 64}}},
    u'ge-0/0/0.0': {   u'ipv4': {   u'192.168.0.30': {   u'prefix_length': 24}}},
    u'ge-0/0/1.0': {   u'ipv4': {   u'172.16.0.30': {   u'prefix_length': 24}}},
    u'lo0.16384': {   u'ipv4': {   u'127.0.0.1': {   u'prefix_length': 32}}},
    u'lo0.16385': {   u'ipv4': {   u'128.0.0.1': {   u'prefix_length': 32},
                                   u'128.0.0.4': {   u'prefix_length': 32}},
                      u'ipv6': {   u'fe80::20c:290f:fc88:f0c4': {   u'prefix_length': 128}}}}


JSON dumps print: 

{
    "lo0.16384": {
        "ipv4": {
            "127.0.0.1": {
                "prefix_length": 32
            }
        }
    }, 
    "ge-0/0/0.0": {
        "ipv4": {
            "192.168.0.30": {
                "prefix_length": 24
            }
        }
    }, 
    "em1.0": {
        "ipv4": {
            "172.16.0.1": {
                "prefix_length": 16
            }
        }, 
        "ipv6": {
            "fe80::20c:29ff:fe88:f0ce": {
                "prefix_length": 64
            }
        }
    }, 
    "lo0.16385": {
        "ipv4": {
            "128.0.0.4": {
                "prefix_length": 32
            }, 
            "128.0.0.1": {
                "prefix_length": 32
            }
        }, 
        "ipv6": {
            "fe80::20c:290f:fc88:f0c4": {
                "prefix_length": 128
            }
        }
    }, 
    "ge-0/0/1.0": {
        "ipv4": {
            "172.16.0.30": {
                "prefix_length": 24
            }
        }
    }
}
------------------------------------------------------------
------------------------------------------------------------
```

- get_lldp_neighbors:
```
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_1/configuration/get_lldp_neighbors.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
Raw print: 

{   u'Ethernet1': [{   u'hostname': u'lon.vmx1', u'port': u'515'}],
    u'Management1': [{   u'hostname': u'lon.vmx1', u'port': u'514'}]}


JSON dumps print: 

{
    "Management1": [
        {
            "hostname": "lon.vmx1", 
            "port": "514"
        }
    ], 
    "Ethernet1": [
        {
            "hostname": "lon.vmx1", 
            "port": "515"
        }
    ]
}
------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
Raw print: 

{   'ge-0/0/0': [{   'hostname': u'par.arista1', 'port': u'Management1'}],
    'ge-0/0/1': [{   'hostname': u'par.arista1', 'port': u'Ethernet1'}]}


JSON dumps print: 

{
    "ge-0/0/1": [
        {
            "hostname": "par.arista1", 
            "port": "Ethernet1"
        }
    ], 
    "ge-0/0/0": [
        {
            "hostname": "par.arista1", 
            "port": "Management1"
        }
    ]
}
------------------------------------------------------------
------------------------------------------------------------
```


## Setters (configuration commands):

- change_hostname:

```
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_1/configuration/change_hostname.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
@@ -7,7 +7,7 @@
 logging host 192.168.0.125 49017
 logging source-interface Ethernet1
 !
-hostname par.arista1
+hostname arista1
 !
 spanning-tree mode mstp
 !
------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
[edit system]
-  host-name lon.vmx1;
+  host-name vmx1;
------------------------------------------------------------
------------------------------------------------------------
mab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_1/configuration/change_hostname.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------

------------------------------------------------------------
Device : vmx1
------------------------------------------------------------

------------------------------------------------------------
------------------------------------------------------------
mab@mab-infra:~$ 
```

- cfg_bgp:
```
mab@mab-infra:~$ sudo python mab_automate/napalm/labs/napalm-python/lab_1/configuration/cfg_bgp.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
rendering bgp template
@@ -26,7 +26,7 @@
 ip routing
 !
 router bgp 65070
-   router-id 70.70.70.71
+   router-id 70.70.70.70
    neighbor 172.16.0.30 remote-as 65030
    neighbor 172.16.0.30 description vmx1
    neighbor 172.16.0.30 maximum-routes 12000
------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
rendering bgp template
[edit routing-options]
-  router-id 30.30.30.31;
+  router-id 30.30.30.30;
------------------------------------------------------------
------------------------------------------------------------
mab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ sudo python mab_automate/napalm/labs/napalm-python/lab_1/configuration/cfg_bgp.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
rendering bgp template

------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
rendering bgp template

------------------------------------------------------------
------------------------------------------------------------
```

## Validation:

- basic_env:
```
mab@mab-infra:~$ sudo python mab_automate/napalm/labs/napalm-python/lab_1/validation/validate_basic_env.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
{u'complies': False,
 'get_facts': {u'complies': False,
               u'extra': [],
               u'missing': [],
               u'present': {'os_version': {u'actual_value': u'4.18.1F-4591672.4181F',
                                           u'complies': False,
                                           u'expected_value': 4.17,
                                           u'nested': False}}},
 'get_interfaces_ip': {u'complies': True,
                       u'extra': [],
                       u'missing': [],
                       u'present': {'Ethernet1': {u'complies': True,
                                                  u'nested': True}}},
 u'skipped': []}
------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
{u'complies': True,
 'get_facts': {u'complies': True,
               u'extra': [],
               u'missing': [],
               u'present': {'os_version': {u'complies': True,
                                           u'nested': False}}},
 'get_interfaces_ip': {u'complies': True,
                       u'extra': [],
                       u'missing': [],
                       u'present': {'ge-0/0/1.0': {u'complies': True,
                                                   u'nested': True}}},
 u'skipped': []}
mab@mab-infra:~$ 
```

- bgp:
```
mab@mab-infra:~$ sudo python mab_automate/napalm/labs/napalm-python/lab_1/validation/validate_bgp.py 
------------------------------------------------------------
Device : arista1
------------------------------------------------------------
{u'complies': False,
 'get_bgp_neighbors_detail': {u'complies': False,
                              u'extra': [],
                              u'missing': [],
                              u'present': {'default': {u'complies': False,
                                                       u'diff': {u'complies': False,
                                                                 u'extra': [],
                                                                 u'missing': [],
                                                                 u'present': {65030: {u'complies': True,
                                                                                      u'nested': False},
                                                                              65040: {u'actual_value': [{u'accepted_prefix_count': 0,
                                                                                                         u'active_prefix_count': 0,
                                                                                                         u'advertised_prefix_count': 0,
                                                                                                         u'configured_holdtime': 180,
                                                                                                         u'configured_keepalive': 60,
                                                                                                         u'connection_state': u'',
                                                                                                         u'export_policy': u'',
                                                                                                         u'flap_count': 0,
                                                                                                         u'holdtime': 180,
                                                                                                         u'import_policy': u'',
                                                                                                         u'input_messages': 0,
                                                                                                         u'input_updates': 0,
                                                                                                         u'keepalive': 60,
                                                                                                         u'last_event': u'Start',
                                                                                                         u'local_address': u'',
                                                                                                         u'local_address_configured': False,
                                                                                                         u'local_as': 65070,
                                                                                                         u'local_as_prepend': False,
                                                                                                         u'local_port': 0,
                                                                                                         u'messages_queued_out': 0,
                                                                                                         u'multihop': True,
                                                                                                         u'multipath': False,
                                                                                                         u'output_messages': 0,
                                                                                                         u'output_updates': 0,
                                                                                                         u'previous_connection_state': u'Active',
                                                                                                         u'received_prefix_count': 0,
                                                                                                         u'remote_address': u'172.16.0.40',
                                                                                                         u'remote_as': 65040,
                                                                                                         u'remote_port': 179,
                                                                                                         u'remove_private_as': False,
                                                                                                         u'router_id': u'0.0.0.0',
                                                                                                         u'routing_table': u'default',
                                                                                                         u'suppress_4byte_as': False,
                                                                                                         u'suppressed_prefix_count': 0,
                                                                                                         u'up': False}],
                                                                                      u'complies': False,
                                                                                      u'expected_value': [{'connection_state': 'Established'}],
                                                                                      u'nested': False},
                                                                              65080: {u'actual_value': [{u'accepted_prefix_count': 0,
                                                                                                         u'active_prefix_count': 0,
                                                                                                         u'advertised_prefix_count': 0,
                                                                                                         u'configured_holdtime': 180,
                                                                                                         u'configured_keepalive': 60,
                                                                                                         u'connection_state': u'',
                                                                                                         u'export_policy': u'',
                                                                                                         u'flap_count': 0,
                                                                                                         u'holdtime': 180,
                                                                                                         u'import_policy': u'',
                                                                                                         u'input_messages': 0,
                                                                                                         u'input_updates': 0,
                                                                                                         u'keepalive': 60,
                                                                                                         u'last_event': u'ConnectRetry',
                                                                                                         u'local_address': u'',
                                                                                                         u'local_address_configured': False,
                                                                                                         u'local_as': 65070,
                                                                                                         u'local_as_prepend': False,
                                                                                                         u'local_port': 0,
                                                                                                         u'messages_queued_out': 0,
                                                                                                         u'multihop': True,
                                                                                                         u'multipath': False,
                                                                                                         u'output_messages': 0,
                                                                                                         u'output_updates': 0,
                                                                                                         u'previous_connection_state': u'Active',
                                                                                                         u'received_prefix_count': 0,
                                                                                                         u'remote_address': u'172.16.0.80',
                                                                                                         u'remote_as': 65080,
                                                                                                         u'remote_port': 179,
                                                                                                         u'remove_private_as': False,
                                                                                                         u'router_id': u'0.0.0.0',
                                                                                                         u'routing_table': u'default',
                                                                                                         u'suppress_4byte_as': False,
                                                                                                         u'suppressed_prefix_count': 0,
                                                                                                         u'up': False}],
                                                                                      u'complies': False,
                                                                                      u'expected_value': [{'connection_state': 'Established'}],
                                                                                      u'nested': False}}},
                                                       u'nested': True}}},
 u'skipped': []}
------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
{u'complies': False,
 'get_bgp_neighbors_detail': {u'complies': False,
                              u'extra': [],
                              u'missing': [],
                              u'present': {'global': {u'complies': False,
                                                      u'diff': {u'complies': False,
                                                                u'extra': [],
                                                                u'missing': [],
                                                                u'present': {65040: {u'actual_value': [{u'accepted_prefix_count': -1,
                                                                                                        u'active_prefix_count': -1,
                                                                                                        u'advertised_prefix_count': -1,
                                                                                                        u'configured_holdtime': 90,
                                                                                                        u'configured_keepalive': 0,
                                                                                                        u'connection_state': u'Active',
                                                                                                        u'export_policy': u'bgp-out',
                                                                                                        u'flap_count': 0,
                                                                                                        u'holdtime': 0,
                                                                                                        u'import_policy': u'bgp-in',
                                                                                                        u'input_messages': -1,
                                                                                                        u'input_updates': -1,
                                                                                                        u'keepalive': 0,
                                                                                                        u'last_event': u'Start',
                                                                                                        u'local_address': u'172.16.0.30',
                                                                                                        u'local_address_configured': False,
                                                                                                        u'local_as': 65030,
                                                                                                        u'local_as_prepend': False,
                                                                                                        u'local_port': 179,
                                                                                                        u'messages_queued_out': 0,
                                                                                                        u'multihop': False,
                                                                                                        u'multipath': True,
                                                                                                        u'output_messages': -1,
                                                                                                        u'output_updates': -1,
                                                                                                        u'previous_connection_state': u'Idle',
                                                                                                        u'received_prefix_count': -1,
                                                                                                        u'remote_address': u'172.16.0.40',
                                                                                                        u'remote_as': 65040,
                                                                                                        u'remote_port': 179,
                                                                                                        u'remove_private_as': False,
                                                                                                        u'router_id': u'',
                                                                                                        u'routing_table': u'global',
                                                                                                        u'suppress_4byte_as': True,
                                                                                                        u'suppressed_prefix_count': -1,
                                                                                                        u'up': False}],
                                                                                     u'complies': False,
                                                                                     u'expected_value': [{'connection_state': 'Established'}],
                                                                                     u'nested': False},
                                                                             65070: {u'complies': True,
                                                                                     u'nested': False},
                                                                             65080: {u'actual_value': [{u'accepted_prefix_count': -1,
                                                                                                        u'active_prefix_count': -1,
                                                                                                        u'advertised_prefix_count': -1,
                                                                                                        u'configured_holdtime': 90,
                                                                                                        u'configured_keepalive': 0,
                                                                                                        u'connection_state': u'Active',
                                                                                                        u'export_policy': u'bgp-out',
                                                                                                        u'flap_count': 0,
                                                                                                        u'holdtime': 0,
                                                                                                        u'import_policy': u'bgp-in',
                                                                                                        u'input_messages': -1,
                                                                                                        u'input_updates': -1,
                                                                                                        u'keepalive': 0,
                                                                                                        u'last_event': u'Start',
                                                                                                        u'local_address': u'172.16.0.30',
                                                                                                        u'local_address_configured': False,
                                                                                                        u'local_as': 65030,
                                                                                                        u'local_as_prepend': False,
                                                                                                        u'local_port': 179,
                                                                                                        u'messages_queued_out': 0,
                                                                                                        u'multihop': False,
                                                                                                        u'multipath': True,
                                                                                                        u'output_messages': -1,
                                                                                                        u'output_updates': -1,
                                                                                                        u'previous_connection_state': u'Idle',
                                                                                                        u'received_prefix_count': -1,
                                                                                                        u'remote_address': u'172.16.0.80',
                                                                                                        u'remote_as': 65080,
                                                                                                        u'remote_port': 179,
                                                                                                        u'remove_private_as': False,
                                                                                                        u'router_id': u'',
                                                                                                        u'routing_table': u'global',
                                                                                                        u'suppress_4byte_as': True,
                                                                                                        u'suppressed_prefix_count': -1,
                                                                                                        u'up': False}],
                                                                                     u'complies': False,
                                                                                     u'expected_value': [{'connection_state': 'Established'}],
                                                                                     u'nested': False}}},
                                                      u'nested': True}}},
 u'skipped': []}
mab@mab-infra:~$ 

```
