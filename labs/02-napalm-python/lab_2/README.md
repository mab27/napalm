# Lab_2

## Overview:
- [Lab_1](https://github.com/mab27/napalm/tree/master/labs/napalm-python/lab_1) optimised with inventory management for better scalability (inventory managed as a python data structure).
- Sections:
	- Same as [Lab_1](https://github.com/mab27/napalm/tree/master/labs/napalm-python/lab_1)

## Getters (show commands):

```
mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$ python configuration/get_bgp_config.py 
------------------------------------------------------------
Device : vmx2
------------------------------------------------------------
 Not able to reach the device 

------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
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


------------------------------------------------------------
Device : arista2
------------------------------------------------------------
No handlers could be found for logger "pyeapi.eapilib"
 Not able to reach the device 

------------------------------------------------------------
Device : arista1
------------------------------------------------------------
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
```

```
mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$ python  configuration/get_bgp_neighbors.py 
------------------------------------------------------------
Device : vmx2
------------------------------------------------------------
 Not able to reach the device 

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
                "uptime": 2265, 
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
                "uptime": 2085, 
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
                "remote_id": "70.70.70.70", 
                "local_as": 65030, 
                "is_up": true, 
                "description": "aritsa1"
            }, 
            "172.16.0.40": {
                "is_enabled": true, 
                "uptime": 2265, 
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


------------------------------------------------------------
Device : arista2
------------------------------------------------------------
No handlers could be found for logger "pyeapi.eapilib"
 Not able to reach the device 

------------------------------------------------------------
Device : arista1
------------------------------------------------------------
JSON dumps print: 

{
    "global": {
        "router_id": "70.70.70.70", 
        "peers": {
            "172.16.0.80": {
                "is_enabled": true, 
                "uptime": -5111, 
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
                "uptime": -5111, 
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
                "uptime": -5112, 
                "remote_as": 65030, 
                "description": "", 
                "remote_id": "30.30.30.30", 
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


mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$
```

```
mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$ python configuration/get_bgp_neighbors_details.py 
------------------------------------------------------------
Device : vmx2
------------------------------------------------------------
 Not able to reach the device 

------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
JSON dumps print: 

{
    "global": {
        "65040": [
            {
                "suppress_4byte_as": true, 
                "local_as_prepend": false, 
                "connection_state": "Connect", 
                "multihop": false, 
                "input_messages": -1, 
                "previous_connection_state": "Active", 
                "output_messages": -1, 
                "remove_private_as": false, 
                "multipath": true, 
                "messages_queued_out": 0, 
                "keepalive": 0, 
                "remote_as": 65040, 
                "local_port": 179, 
                "active_prefix_count": -1, 
                "configured_holdtime": 90, 
                "routing_table": "global", 
                "flap_count": 0, 
                "suppressed_prefix_count": -1, 
                "local_address": "172.16.0.30", 
                "remote_port": 179, 
                "input_updates": -1, 
                "configured_keepalive": 0, 
                "router_id": "", 
                "export_policy": "bgp-out", 
                "local_as": 65030, 
                "remote_address": "172.16.0.40", 
                "advertised_prefix_count": -1, 
                "local_address_configured": false, 
                "import_policy": "bgp-in", 
                "last_event": "ConnectRetry", 
                "accepted_prefix_count": -1, 
                "up": false, 
                "output_updates": -1, 
                "received_prefix_count": -1, 
                "holdtime": 0
            }
        ], 
        "65080": [
            {
                "suppress_4byte_as": true, 
                "local_as_prepend": false, 
                "connection_state": "Connect", 
                "multihop": false, 
                "input_messages": -1, 
                "previous_connection_state": "Active", 
                "output_messages": -1, 
                "remove_private_as": false, 
                "multipath": true, 
                "messages_queued_out": 0, 
                "keepalive": 0, 
                "remote_as": 65080, 
                "local_port": 179, 
                "active_prefix_count": -1, 
                "configured_holdtime": 90, 
                "routing_table": "global", 
                "flap_count": 0, 
                "suppressed_prefix_count": -1, 
                "local_address": "172.16.0.30", 
                "remote_port": 179, 
                "input_updates": -1, 
                "configured_keepalive": 0, 
                "router_id": "", 
                "export_policy": "bgp-out", 
                "local_as": 65030, 
                "remote_address": "172.16.0.80", 
                "advertised_prefix_count": -1, 
                "local_address_configured": false, 
                "import_policy": "bgp-in", 
                "last_event": "ConnectRetry", 
                "accepted_prefix_count": -1, 
                "up": false, 
                "output_updates": -1, 
                "received_prefix_count": -1, 
                "holdtime": 0
            }
        ], 
        "65070": [
            {
                "suppress_4byte_as": false, 
                "local_as_prepend": false, 
                "connection_state": "Established", 
                "multihop": false, 
                "input_messages": 73, 
                "previous_connection_state": "OpenConfirm", 
                "output_messages": 82, 
                "remove_private_as": false, 
                "multipath": true, 
                "messages_queued_out": 0, 
                "keepalive": 30, 
                "remote_as": 65070, 
                "local_port": 179, 
                "active_prefix_count": 0, 
                "configured_holdtime": 90, 
                "routing_table": "global", 
                "flap_count": 0, 
                "suppressed_prefix_count": 0, 
                "local_address": "172.16.0.30", 
                "remote_port": 55549, 
                "input_updates": 1, 
                "configured_keepalive": 30, 
                "router_id": "70.70.70.70", 
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


------------------------------------------------------------
Device : arista2
------------------------------------------------------------
No handlers could be found for logger "pyeapi.eapilib"
 Not able to reach the device 

------------------------------------------------------------
Device : arista1
------------------------------------------------------------
JSON dumps print: 

{
    "default": {
        "65040": [
            {
                "accepted_prefix_count": 0, 
                "suppress_4byte_as": false, 
                "local_as_prepend": false, 
                "export_policy": "", 
                "multihop": true, 
                "input_messages": 0, 
                "previous_connection_state": "Active", 
                "output_messages": 0, 
                "remove_private_as": false, 
                "multipath": false, 
                "messages_queued_out": 0, 
                "keepalive": 60, 
                "remote_as": 65040, 
                "local_port": 0, 
                "active_prefix_count": 0, 
                "configured_holdtime": 180, 
                "routing_table": "default", 
                "flap_count": 0, 
                "suppressed_prefix_count": 0, 
                "local_address": "", 
                "input_updates": 0, 
                "configured_keepalive": 60, 
                "router_id": "0.0.0.0", 
                "connection_state": "", 
                "local_as": 65070, 
                "remote_address": "172.16.0.40", 
                "advertised_prefix_count": 0, 
                "local_address_configured": false, 
                "import_policy": "", 
                "last_event": "Start", 
                "remote_port": 179, 
                "up": false, 
                "output_updates": 0, 
                "received_prefix_count": 0, 
                "holdtime": 180
            }
        ], 
        "65080": [
            {
                "accepted_prefix_count": 0, 
                "suppress_4byte_as": false, 
                "local_as_prepend": false, 
                "export_policy": "", 
                "multihop": true, 
                "input_messages": 0, 
                "previous_connection_state": "Active", 
                "output_messages": 0, 
                "remove_private_as": false, 
                "multipath": false, 
                "messages_queued_out": 0, 
                "keepalive": 60, 
                "remote_as": 65080, 
                "local_port": 0, 
                "active_prefix_count": 0, 
                "configured_holdtime": 180, 
                "routing_table": "default", 
                "flap_count": 0, 
                "suppressed_prefix_count": 0, 
                "local_address": "", 
                "input_updates": 0, 
                "configured_keepalive": 60, 
                "router_id": "0.0.0.0", 
                "connection_state": "", 
                "local_as": 65070, 
                "remote_address": "172.16.0.80", 
                "advertised_prefix_count": 0, 
                "local_address_configured": false, 
                "import_policy": "", 
                "last_event": "Start", 
                "remote_port": 179, 
                "up": false, 
                "output_updates": 0, 
                "received_prefix_count": 0, 
                "holdtime": 180
            }
        ], 
        "65030": [
            {
                "accepted_prefix_count": 2, 
                "suppress_4byte_as": false, 
                "local_as_prepend": false, 
                "export_policy": "", 
                "multihop": true, 
                "input_messages": 84, 
                "previous_connection_state": "OpenConfirm", 
                "output_messages": 74, 
                "remove_private_as": false, 
                "multipath": false, 
                "messages_queued_out": 0, 
                "keepalive": 30, 
                "remote_as": 65030, 
                "local_port": 55549, 
                "active_prefix_count": 0, 
                "configured_holdtime": 180, 
                "routing_table": "default", 
                "flap_count": 0, 
                "suppressed_prefix_count": 0, 
                "local_address": "172.16.0.70", 
                "input_updates": 2, 
                "configured_keepalive": 60, 
                "router_id": "30.30.30.30", 
                "connection_state": "Established", 
                "local_as": 65070, 
                "remote_address": "172.16.0.30", 
                "advertised_prefix_count": 0, 
                "local_address_configured": true, 
                "import_policy": "", 
                "last_event": "RecvKeepAlive", 
                "remote_port": 179, 
                "up": true, 
                "output_updates": 1, 
                "received_prefix_count": 2, 
                "holdtime": 90
            }
        ]
    }
}


mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$
```

```
```

```
```

```
```

## Setters (configuration validation):

```
mab@mab-infra:~$ python mab_automate/napalm/labs/napalm-python/lab_2/configuration/cfg_bgp.py 
------------------------------------------------------------
Device : vmx2
------------------------------------------------------------
 - Getting template
 - Getting variables
 Not able to find variables for the device 

------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
 - Getting template
 - Getting variables
 - Rendering bgp template
 - Creating Device object
 - Configuring Device

------------------------------------------------------------
Device : arista2
------------------------------------------------------------
 - Getting template
 - Getting variables
 Not able to find variables for the device 

------------------------------------------------------------
Device : arista1
------------------------------------------------------------
 - Getting template
 - Getting variables
 - Rendering bgp template
 - Creating Device object
 - Configuring Device

------------------------------------------------------------
Audit will start in 15 seconds
------------------------------------------------------------


------------------------------------------------------------
Printing bgp sessions state for device vmx2
------------------------------------------------------------
 Not able to find variables for the device 

------------------------------------------------------------
Printing bgp sessions state for device vmx1
------------------------------------------------------------
 Peer 172.16.0.40 is Connect
 Peer 172.16.0.80 is Connect
 Peer 172.16.0.70 is Established
------------------------------------------------------------
Printing bgp sessions state for device arista2
------------------------------------------------------------
No handlers could be found for logger "pyeapi.eapilib"
 Not able to find variables for the device 

------------------------------------------------------------
Printing bgp sessions state for device arista1
------------------------------------------------------------
 Peer 172.16.0.40 is 
 Peer 172.16.0.80 is 
 Peer 172.16.0.30 is Established
```

## validation:

### basic_env:

```
mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$ python validation/validate_basic_env.py 
------------------------------------------------------------
Device : vmx2
------------------------------------------------------------
 Validation file : /home/mab/mab_automate/napalm/labs/02-napalm-python/lab_2/validation/validate_files//vmx2_basic_env.yml
 Not able to reach the device 

------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
 Validation file : /home/mab/mab_automate/napalm/labs/02-napalm-python/lab_2/validation/validate_files//vmx1_basic_env.yml
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
------------------------------------------------------------
Device : arista2
------------------------------------------------------------
 Validation file : /home/mab/mab_automate/napalm/labs/02-napalm-python/lab_2/validation/validate_files//arista2_basic_env.yml
No handlers could be found for logger "pyeapi.eapilib"
 Not able to reach the device 

------------------------------------------------------------
Device : arista1
------------------------------------------------------------
 Validation file : /home/mab/mab_automate/napalm/labs/02-napalm-python/lab_2/validation/validate_files//arista1_basic_env.yml
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
mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$ 
```

### bgp:

```
mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$ python validation/validate_bgp.py 
------------------------------------------------------------
Device : vmx2
------------------------------------------------------------
 Validation file : /home/mab/mab_automate/napalm/labs/02-napalm-python/lab_2/validation/validate_files//vmx2_bgp.yml
 Not able to reach the device 

------------------------------------------------------------
Device : vmx1
------------------------------------------------------------
 Validation file : /home/mab/mab_automate/napalm/labs/02-napalm-python/lab_2/validation/validate_files//vmx1_bgp.yml
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
                                                                                                        u'connection_state': u'Connect',
                                                                                                        u'export_policy': u'bgp-out',
                                                                                                        u'flap_count': 0,
                                                                                                        u'holdtime': 0,
                                                                                                        u'import_policy': u'bgp-in',
                                                                                                        u'input_messages': -1,
                                                                                                        u'input_updates': -1,
                                                                                                        u'keepalive': 0,
                                                                                                        u'last_event': u'ConnectRetry',
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
                                                                                                        u'previous_connection_state': u'Active',
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
                                                                                                        u'connection_state': u'Connect',
                                                                                                        u'export_policy': u'bgp-out',
                                                                                                        u'flap_count': 0,
                                                                                                        u'holdtime': 0,
                                                                                                        u'import_policy': u'bgp-in',
                                                                                                        u'input_messages': -1,
                                                                                                        u'input_updates': -1,
                                                                                                        u'keepalive': 0,
                                                                                                        u'last_event': u'ConnectRetry',
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
                                                                                                        u'previous_connection_state': u'Active',
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
------------------------------------------------------------
Device : arista2
------------------------------------------------------------
 Validation file : /home/mab/mab_automate/napalm/labs/02-napalm-python/lab_2/validation/validate_files//arista2_bgp.yml
No handlers could be found for logger "pyeapi.eapilib"
 Not able to reach the device 

------------------------------------------------------------
Device : arista1
------------------------------------------------------------
 Validation file : /home/mab/mab_automate/napalm/labs/02-napalm-python/lab_2/validation/validate_files//arista1_bgp.yml
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
mab@mab-infra:~/mab_automate/napalm/labs/02-napalm-python/lab_2$ 

```
