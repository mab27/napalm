from napalm_base import get_network_driver
import napalm_yang
from json import dumps
from pprint import pprint

# Create Device Object
junos_driver = get_network_driver('junos')

junos_device = {
	'hostname': '192.168.0.30',
	'username': 'mab',
	'password': 'mab123',
}

with junos_driver(**junos_device) as d:
	running_config = napalm_yang.base.Root()
	running_config.add_model(napalm_yang.models.openconfig_interfaces)
	running_config.parse_config(device=d)

print dumps(running_config.get(filter=True), indent=4)

"""
mab@mab-infra:~/mab_automate/napalm/sample_script_files$ python napalm_oc.py 
No handlers could be found for logger "napalm-yang"
{
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
                                        "192.168.0.30": {
                                            "ip": "192.168.0.30", 
                                            "config": {
                                                "ip": "192.168.0.30", 
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
            }, 
            "ge-0/0/1": {
                "name": "ge-0/0/1", 
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
                                        "172.16.0.30": {
                                            "ip": "172.16.0.30", 
                                            "config": {
                                                "ip": "172.16.0.30", 
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
                    "name": "ge-0/0/1"
                }
            }
        }
    }
}

"""