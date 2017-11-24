# Lab_1:

## Overview:
- Ansible playbooks using NAPALM modules.
- Sections:
    - [Getters (show commands)](https://github.com/mab27/napalm/tree/master/labs/04-napalm-ansible/lab_1#getters-show-commands)
    	- [get_facts](https://github.com/mab27/napalm/tree/master/labs/04-napalm-ansible/lab_1#get_facts)
        - [get_facts (interfaces)](https://github.com/mab27/napalm/tree/master/labs/04-napalm-ansible/lab_1#get_facts-interfaces)
      	- [get_facts (bgp_neighbors)](https://github.com/mab27/napalm/tree/master/labs/04-napalm-ansible/lab_1#get_facts-bgp_neighbors)
        - [get_facts (bgp_neighbors_detail)](https://github.com/mab27/napalm/tree/master/labs/04-napalm-ansible/lab_1#get_facts-bgp_neighbors_detail)
    - [Setters (configuration and validations commands)](https://github.com/mab27/napalm/tree/master/labs/04-napalm-ansible/lab_1#setters-configuration-commands)
    	- [install_config](https://github.com/mab27/napalm/tree/master/labs/04-napalm-ansible/lab_1#install_config)

## Getters (show commands):

### get_facts:
```
mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ ansible-playbook pb_get_facts.yml 

PLAY [Get facts] *******************************************************************************************************************************************************************************************

TASK [Get facts from device] *******************************************************************************************************************************************************************************
ok: [arista1]
fatal: [vmx2]: FAILED! => {"changed": false, "failed": true, "msg": "cannot connect to device: ConnectRefusedError(192.168.0.40)"}
fatal: [arista2]: FAILED! => {"changed": false, "failed": true, "msg": "cannot connect to device: Socket error during eAPI connection: [Errno 113] No route to host"}
ok: [vmx1]

TASK [print data] ******************************************************************************************************************************************************************************************
ok: [arista1] => {
    "result": {
        "ansible_facts": {
            "napalm_facts": {
                "fqdn": "arista1", 
                "hostname": "arista1", 
                "interface_list": [
                    "Ethernet1", 
                    "Management1"
                ], 
                "model": "vEOS", 
                "os_version": "4.18.1F-4591672.4181F", 
                "serial_number": "", 
                "uptime": -4020, 
                "vendor": "Arista"
            }, 
            "napalm_fqdn": "arista1", 
            "napalm_hostname": "arista1", 
            "napalm_interface_list": [
                "Ethernet1", 
                "Management1"
            ], 
            "napalm_model": "vEOS", 
            "napalm_os_version": "4.18.1F-4591672.4181F", 
            "napalm_serial_number": "", 
            "napalm_uptime": -4020, 
            "napalm_vendor": "Arista"
        }, 
        "changed": false, 
        "failed": false
    }
}
ok: [vmx1] => {
    "result": {
        "ansible_facts": {
            "napalm_facts": {
                "fqdn": "vmx1", 
                "hostname": "vmx1", 
                "interface_list": [
                    "ge-0/0/0", 
                    "lc-0/0/0", 
                    "pfe-0/0/0", 
                    "pfh-0/0/0", 
                    "ge-0/0/1", 
                    "ge-0/0/2", 
                    "ge-0/0/3", 
                    "ge-0/0/4", 
                    "ge-0/0/5", 
                    "ge-0/0/6", 
                    "ge-0/0/7", 
                    "ge-0/0/8", 
                    "ge-0/0/9", 
                    ".local.", 
                    "cbp0", 
                    "demux0", 
                    "dsc", 
                    "em1", 
                    "em2", 
                    "em3", 
                    "em4", 
                    "em5", 
                    "em6", 
                    "em7", 
                    "em8", 
                    "em9", 
                    "fxp0", 
                    "gre", 
                    "ipip", 
                    "irb", 
                    "lo0", 
                    "lsi", 
                    "mtun", 
                    "pimd", 
                    "pime", 
                    "pip0", 
                    "pp0", 
                    "tap", 
                    "vtep"
                ], 
                "model": "VMX", 
                "os_version": "14.1R4.9", 
                "serial_number": "VM55E771B3CD", 
                "uptime": 3443, 
                "vendor": "Juniper"
            }, 
            "napalm_fqdn": "vmx1", 
            "napalm_hostname": "vmx1", 
            "napalm_interface_list": [
                "ge-0/0/0", 
                "lc-0/0/0", 
                "pfe-0/0/0", 
                "pfh-0/0/0", 
                "ge-0/0/1", 
                "ge-0/0/2", 
                "ge-0/0/3", 
                "ge-0/0/4", 
                "ge-0/0/5", 
                "ge-0/0/6", 
                "ge-0/0/7", 
                "ge-0/0/8", 
                "ge-0/0/9", 
                ".local.", 
                "cbp0", 
                "demux0", 
                "dsc", 
                "em1", 
                "em2", 
                "em3", 
                "em4", 
                "em5", 
                "em6", 
                "em7", 
                "em8", 
                "em9", 
                "fxp0", 
                "gre", 
                "ipip", 
                "irb", 
                "lo0", 
                "lsi", 
                "mtun", 
                "pimd", 
                "pime", 
                "pip0", 
                "pp0", 
                "tap", 
                "vtep"
            ], 
            "napalm_model": "VMX", 
            "napalm_os_version": "14.1R4.9", 
            "napalm_serial_number": "VM55E771B3CD", 
            "napalm_uptime": 3443, 
            "napalm_vendor": "Juniper"
        }, 
        "changed": false, 
        "failed": false
    }
}
 [WARNING]: Could not create retry file '/home/mab/mab_automate/napalm/labs/04-napalm-ansible/pb_get_facts.retry'.         [Errno 13] Permission denied: u'/home/mab/mab_automate/napalm/labs/04-napalm-
ansible/pb_get_facts.retry'


PLAY RECAP *************************************************************************************************************************************************************************************************
arista1                    : ok=2    changed=0    unreachable=0    failed=0   
arista2                    : ok=0    changed=0    unreachable=0    failed=1   
vmx1                       : ok=2    changed=0    unreachable=0    failed=0   
vmx2                       : ok=0    changed=0    unreachable=0    failed=1   

mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$
```

### get_facts (interfaces):
```
mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ ansible-playbook lab_1/pb_get_facts.yml 

PLAY [Get facts] *******************************************************************************************************************************************************************************************

TASK [Get facts from device] *******************************************************************************************************************************************************************************
ok: [arista1]
fatal: [vmx2]: FAILED! => {"changed": false, "failed": true, "msg": "cannot connect to device: ConnectRefusedError(192.168.0.40)"}
fatal: [arista2]: FAILED! => {"changed": false, "failed": true, "msg": "cannot connect to device: Socket error during eAPI connection: [Errno 113] No route to host"}
ok: [vmx1]

TASK [print data] ******************************************************************************************************************************************************************************************
ok: [arista1] => {
    "result": {
        "ansible_facts": {
            "napalm_interfaces": {
                "Ethernet1": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 1511541147.7177436, 
                    "mac_address": "00:0C:29:FA:C2:C1", 
                    "speed": 0
                }, 
                "Management1": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 1511541144.5403194, 
                    "mac_address": "00:0C:29:69:72:9E", 
                    "speed": 1000
                }
            }
        }, 
        "changed": false, 
        "failed": false
    }
}
ok: [vmx1] => {
    "result": {
        "ansible_facts": {
            "napalm_interfaces": {
                ".local.": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": -1
                }, 
                "cbp0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:05:86:71:40:11", 
                    "speed": -1
                }, 
                "demux0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": -1
                }, 
                "dsc": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": -1
                }, 
                "em1": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:CE", 
                    "speed": 1000
                }, 
                "em2": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:D8", 
                    "speed": 1000
                }, 
                "em3": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:E2", 
                    "speed": 1000
                }, 
                "em4": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:EC", 
                    "speed": 1000
                }, 
                "em5": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:F6", 
                    "speed": 1000
                }, 
                "em6": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:00", 
                    "speed": 1000
                }, 
                "em7": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:0A", 
                    "speed": 1000
                }, 
                "em8": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:14", 
                    "speed": 1000
                }, 
                "em9": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:0C:29:88:F0:1E", 
                    "speed": 1000
                }, 
                "fxp0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5089.0, 
                    "mac_address": "00:0C:29:88:F0:C4", 
                    "speed": 1000
                }, 
                "ge-0/0/0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5043.0, 
                    "mac_address": "00:05:86:71:40:00", 
                    "speed": 1000
                }, 
                "ge-0/0/1": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5043.0, 
                    "mac_address": "00:05:86:71:40:01", 
                    "speed": 1000
                }, 
                "ge-0/0/2": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5043.0, 
                    "mac_address": "00:05:86:71:40:02", 
                    "speed": 1000
                }, 
                "ge-0/0/3": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5043.0, 
                    "mac_address": "00:05:86:71:40:03", 
                    "speed": 1000
                }, 
                "ge-0/0/4": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5043.0, 
                    "mac_address": "00:05:86:71:40:04", 
                    "speed": 1000
                }, 
                "ge-0/0/5": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5043.0, 
                    "mac_address": "00:05:86:71:40:05", 
                    "speed": 1000
                }, 
                "ge-0/0/6": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5042.0, 
                    "mac_address": "00:05:86:71:40:06", 
                    "speed": 1000
                }, 
                "ge-0/0/7": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5042.0, 
                    "mac_address": "00:05:86:71:40:07", 
                    "speed": 1000
                }, 
                "ge-0/0/8": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5042.0, 
                    "mac_address": "00:05:86:71:40:08", 
                    "speed": 1000
                }, 
                "ge-0/0/9": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": 5042.0, 
                    "mac_address": "00:05:86:71:40:09", 
                    "speed": 1000
                }, 
                "gre": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "None", 
                    "speed": -1
                }, 
                "ipip": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "None", 
                    "speed": -1
                }, 
                "irb": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:05:86:71:43:F0", 
                    "speed": -1
                }, 
                "lc-0/0/0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": 800
                }, 
                "lo0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": -1
                }, 
                "lsi": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": -1
                }, 
                "mtun": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "None", 
                    "speed": -1
                }, 
                "pfe-0/0/0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": 800
                }, 
                "pfh-0/0/0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": 800
                }, 
                "pimd": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "None", 
                    "speed": -1
                }, 
                "pime": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "None", 
                    "speed": -1
                }, 
                "pip0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "00:05:86:71:43:B0", 
                    "speed": -1
                }, 
                "pp0": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": -1
                }, 
                "tap": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": -1
                }, 
                "vtep": {
                    "description": "", 
                    "is_enabled": true, 
                    "is_up": true, 
                    "last_flapped": -1.0, 
                    "mac_address": "Unspecified", 
                    "speed": -1
                }
            }
        }, 
        "changed": false, 
        "failed": false
    }
}
 [WARNING]: Could not create retry file '/home/mab/mab_automate/napalm/labs/04-napalm-ansible/lab_1/pb_get_facts.retry'.         [Errno 13] Permission denied: u'/home/mab/mab_automate/napalm/labs/04
-napalm-ansible/lab_1/pb_get_facts.retry'


PLAY RECAP *************************************************************************************************************************************************************************************************
arista1                    : ok=2    changed=0    unreachable=0    failed=0   
arista2                    : ok=0    changed=0    unreachable=0    failed=1   
vmx1                       : ok=2    changed=0    unreachable=0    failed=0   
vmx2                       : ok=0    changed=0    unreachable=0    failed=1   

mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ 
```


### get_facts (bgp_neighbors):
```
mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ ansible-playbook lab_1/pb_get_facts.yml 

PLAY [Get facts] *******************************************************************************************************************************************************************************************

TASK [Get facts from device] *******************************************************************************************************************************************************************************
ok: [arista1]
ok: [vmx1]
fatal: [arista2]: FAILED! => {"changed": false, "failed": true, "msg": "cannot connect to device: Socket error during eAPI connection: [Errno 113] No route to host"}
fatal: [vmx2]: FAILED! => {"changed": false, "failed": true, "msg": "cannot connect to device: ConnectRefusedError(192.168.0.40)"}

TASK [print data] ******************************************************************************************************************************************************************************************
ok: [arista1] => {
    "result": {
        "ansible_facts": {
            "napalm_bgp_neighbors": {
                "global": {
                    "peers": {
                        "172.16.0.30": {
                            "address_family": {
                                "ipv4": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": 2, 
                                    "sent_prefixes": 0
                                }, 
                                "ipv6": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": 0, 
                                    "sent_prefixes": 0
                                }
                            }, 
                            "description": "", 
                            "is_enabled": true, 
                            "is_up": true, 
                            "local_as": 65070, 
                            "remote_as": 65030, 
                            "remote_id": "30.30.30.30", 
                            "uptime": -5921
                        }, 
                        "172.16.0.40": {
                            "address_family": {
                                "ipv4": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": 0, 
                                    "sent_prefixes": 0
                                }, 
                                "ipv6": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": 0, 
                                    "sent_prefixes": 0
                                }
                            }, 
                            "description": "", 
                            "is_enabled": true, 
                            "is_up": false, 
                            "local_as": 65070, 
                            "remote_as": 65040, 
                            "remote_id": "0.0.0.0", 
                            "uptime": -5919
                        }, 
                        "172.16.0.80": {
                            "address_family": {
                                "ipv4": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": 0, 
                                    "sent_prefixes": 0
                                }, 
                                "ipv6": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": 0, 
                                    "sent_prefixes": 0
                                }
                            }, 
                            "description": "", 
                            "is_enabled": true, 
                            "is_up": false, 
                            "local_as": 65070, 
                            "remote_as": 65080, 
                            "remote_id": "0.0.0.0", 
                            "uptime": -5919
                        }
                    }, 
                    "router_id": "70.70.70.70"
                }
            }
        }, 
        "changed": false, 
        "failed": false
    }
}
ok: [vmx1] => {
    "result": {
        "ansible_facts": {
            "napalm_bgp_neighbors": {
                "global": {
                    "peers": {
                        "172.16.0.40": {
                            "address_family": {
                                "ipv4": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": -1, 
                                    "sent_prefixes": -1
                                }, 
                                "ipv6": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": -1, 
                                    "sent_prefixes": -1
                                }
                            }, 
                            "description": "vmx2", 
                            "is_enabled": true, 
                            "is_up": false, 
                            "local_as": 65030, 
                            "remote_as": 65040, 
                            "remote_id": "", 
                            "uptime": 1474
                        }, 
                        "172.16.0.70": {
                            "address_family": {
                                "ipv4": {
                                    "accepted_prefixes": 0, 
                                    "received_prefixes": 0, 
                                    "sent_prefixes": 2
                                }, 
                                "ipv6": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": -1, 
                                    "sent_prefixes": -1
                                }
                            }, 
                            "description": "aritsa1", 
                            "is_enabled": true, 
                            "is_up": true, 
                            "local_as": 65030, 
                            "remote_as": 65070, 
                            "remote_id": "70.70.70.70", 
                            "uptime": 1279
                        }, 
                        "172.16.0.80": {
                            "address_family": {
                                "ipv4": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": -1, 
                                    "sent_prefixes": -1
                                }, 
                                "ipv6": {
                                    "accepted_prefixes": -1, 
                                    "received_prefixes": -1, 
                                    "sent_prefixes": -1
                                }
                            }, 
                            "description": "aritsa2", 
                            "is_enabled": true, 
                            "is_up": false, 
                            "local_as": 65030, 
                            "remote_as": 65080, 
                            "remote_id": "", 
                            "uptime": 1474
                        }
                    }, 
                    "router_id": ""
                }
            }
        }, 
        "changed": false, 
        "failed": false
    }
}
 [WARNING]: Could not create retry file '/home/mab/mab_automate/napalm/labs/04-napalm-ansible/lab_1/pb_get_facts.retry'.         [Errno 13] Permission denied: u'/home/mab/mab_automate/napalm/labs/04
-napalm-ansible/lab_1/pb_get_facts.retry'


PLAY RECAP *************************************************************************************************************************************************************************************************
arista1                    : ok=2    changed=0    unreachable=0    failed=0   
arista2                    : ok=0    changed=0    unreachable=0    failed=1   
vmx1                       : ok=2    changed=0    unreachable=0    failed=0   
vmx2                       : ok=0    changed=0    unreachable=0    failed=1   

mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ 
```



### get_facts (bgp_neighbors_detail):
```
mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ ansible-playbook lab_1/pb_get_facts.yml 

PLAY [Get facts] *******************************************************************************************************************************************************************************************

TASK [Get facts from device] *******************************************************************************************************************************************************************************
ok: [arista1]
ok: [vmx1]
fatal: [arista2]: FAILED! => {"changed": false, "failed": true, "msg": "cannot connect to device: Socket error during eAPI connection: [Errno 113] No route to host"}
fatal: [vmx2]: FAILED! => {"changed": false, "failed": true, "msg": "cannot connect to device: ConnectRefusedError(192.168.0.40)"}

TASK [print data] ******************************************************************************************************************************************************************************************
ok: [arista1] => {
    "result": {
        "ansible_facts": {
            "napalm_bgp_neighbors_detail": {
                "default": {
                    "65030": [
                        {
                            "accepted_prefix_count": 2, 
                            "active_prefix_count": 0, 
                            "advertised_prefix_count": 0, 
                            "configured_holdtime": 180, 
                            "configured_keepalive": 60, 
                            "connection_state": "Established", 
                            "export_policy": "", 
                            "flap_count": 0, 
                            "holdtime": 90, 
                            "import_policy": "", 
                            "input_messages": 56, 
                            "input_updates": 2, 
                            "keepalive": 30, 
                            "last_event": "RecvKeepAlive", 
                            "local_address": "172.16.0.70", 
                            "local_address_configured": true, 
                            "local_as": 65070, 
                            "local_as_prepend": false, 
                            "local_port": 55291, 
                            "messages_queued_out": 0, 
                            "multihop": true, 
                            "multipath": false, 
                            "output_messages": 51, 
                            "output_updates": 1, 
                            "previous_connection_state": "OpenConfirm", 
                            "received_prefix_count": 2, 
                            "remote_address": "172.16.0.30", 
                            "remote_as": 65030, 
                            "remote_port": 179, 
                            "remove_private_as": false, 
                            "router_id": "30.30.30.30", 
                            "routing_table": "default", 
                            "suppress_4byte_as": false, 
                            "suppressed_prefix_count": 0, 
                            "up": true
                        }
                    ], 
                    "65040": [
                        {
                            "accepted_prefix_count": 0, 
                            "active_prefix_count": 0, 
                            "advertised_prefix_count": 0, 
                            "configured_holdtime": 180, 
                            "configured_keepalive": 60, 
                            "connection_state": "", 
                            "export_policy": "", 
                            "flap_count": 0, 
                            "holdtime": 180, 
                            "import_policy": "", 
                            "input_messages": 0, 
                            "input_updates": 0, 
                            "keepalive": 60, 
                            "last_event": "Start", 
                            "local_address": "", 
                            "local_address_configured": false, 
                            "local_as": 65070, 
                            "local_as_prepend": false, 
                            "local_port": 0, 
                            "messages_queued_out": 0, 
                            "multihop": true, 
                            "multipath": false, 
                            "output_messages": 0, 
                            "output_updates": 0, 
                            "previous_connection_state": "Active", 
                            "received_prefix_count": 0, 
                            "remote_address": "172.16.0.40", 
                            "remote_as": 65040, 
                            "remote_port": 179, 
                            "remove_private_as": false, 
                            "router_id": "0.0.0.0", 
                            "routing_table": "default", 
                            "suppress_4byte_as": false, 
                            "suppressed_prefix_count": 0, 
                            "up": false
                        }
                    ], 
                    "65080": [
                        {
                            "accepted_prefix_count": 0, 
                            "active_prefix_count": 0, 
                            "advertised_prefix_count": 0, 
                            "configured_holdtime": 180, 
                            "configured_keepalive": 60, 
                            "connection_state": "", 
                            "export_policy": "", 
                            "flap_count": 0, 
                            "holdtime": 180, 
                            "import_policy": "", 
                            "input_messages": 0, 
                            "input_updates": 0, 
                            "keepalive": 60, 
                            "last_event": "Start", 
                            "local_address": "", 
                            "local_address_configured": false, 
                            "local_as": 65070, 
                            "local_as_prepend": false, 
                            "local_port": 0, 
                            "messages_queued_out": 0, 
                            "multihop": true, 
                            "multipath": false, 
                            "output_messages": 0, 
                            "output_updates": 0, 
                            "previous_connection_state": "Active", 
                            "received_prefix_count": 0, 
                            "remote_address": "172.16.0.80", 
                            "remote_as": 65080, 
                            "remote_port": 179, 
                            "remove_private_as": false, 
                            "router_id": "0.0.0.0", 
                            "routing_table": "default", 
                            "suppress_4byte_as": false, 
                            "suppressed_prefix_count": 0, 
                            "up": false
                        }
                    ]
                }
            }
        }, 
        "changed": false, 
        "failed": false
    }
}
ok: [vmx1] => {
    "result": {
        "ansible_facts": {
            "napalm_bgp_neighbors_detail": {
                "global": {
                    "65040": [
                        {
                            "accepted_prefix_count": -1, 
                            "active_prefix_count": -1, 
                            "advertised_prefix_count": -1, 
                            "configured_holdtime": 90, 
                            "configured_keepalive": 0, 
                            "connection_state": "Connect", 
                            "export_policy": "bgp-out", 
                            "flap_count": 0, 
                            "holdtime": 0, 
                            "import_policy": "bgp-in", 
                            "input_messages": -1, 
                            "input_updates": -1, 
                            "keepalive": 0, 
                            "last_event": "ConnectRetry", 
                            "local_address": "172.16.0.30", 
                            "local_address_configured": false, 
                            "local_as": 65030, 
                            "local_as_prepend": false, 
                            "local_port": 179, 
                            "messages_queued_out": 0, 
                            "multihop": false, 
                            "multipath": true, 
                            "output_messages": -1, 
                            "output_updates": -1, 
                            "previous_connection_state": "Active", 
                            "received_prefix_count": -1, 
                            "remote_address": "172.16.0.40", 
                            "remote_as": 65040, 
                            "remote_port": 179, 
                            "remove_private_as": false, 
                            "router_id": "", 
                            "routing_table": "global", 
                            "suppress_4byte_as": true, 
                            "suppressed_prefix_count": -1, 
                            "up": false
                        }
                    ], 
                    "65070": [
                        {
                            "accepted_prefix_count": 0, 
                            "active_prefix_count": 0, 
                            "advertised_prefix_count": 2, 
                            "configured_holdtime": 90, 
                            "configured_keepalive": 30, 
                            "connection_state": "Established", 
                            "export_policy": "bgp-out", 
                            "flap_count": 0, 
                            "holdtime": 90, 
                            "import_policy": "bgp-in", 
                            "input_messages": 50, 
                            "input_updates": 1, 
                            "keepalive": 30, 
                            "last_event": "RecvKeepAlive", 
                            "local_address": "172.16.0.30", 
                            "local_address_configured": false, 
                            "local_as": 65030, 
                            "local_as_prepend": false, 
                            "local_port": 179, 
                            "messages_queued_out": 0, 
                            "multihop": false, 
                            "multipath": true, 
                            "output_messages": 55, 
                            "output_updates": 1, 
                            "previous_connection_state": "OpenConfirm", 
                            "received_prefix_count": 0, 
                            "remote_address": "172.16.0.70", 
                            "remote_as": 65070, 
                            "remote_port": 55291, 
                            "remove_private_as": false, 
                            "router_id": "70.70.70.70", 
                            "routing_table": "global", 
                            "suppress_4byte_as": false, 
                            "suppressed_prefix_count": 0, 
                            "up": true
                        }
                    ], 
                    "65080": [
                        {
                            "accepted_prefix_count": -1, 
                            "active_prefix_count": -1, 
                            "advertised_prefix_count": -1, 
                            "configured_holdtime": 90, 
                            "configured_keepalive": 0, 
                            "connection_state": "Connect", 
                            "export_policy": "bgp-out", 
                            "flap_count": 0, 
                            "holdtime": 0, 
                            "import_policy": "bgp-in", 
                            "input_messages": -1, 
                            "input_updates": -1, 
                            "keepalive": 0, 
                            "last_event": "ConnectRetry", 
                            "local_address": "172.16.0.30", 
                            "local_address_configured": false, 
                            "local_as": 65030, 
                            "local_as_prepend": false, 
                            "local_port": 179, 
                            "messages_queued_out": 0, 
                            "multihop": false, 
                            "multipath": true, 
                            "output_messages": -1, 
                            "output_updates": -1, 
                            "previous_connection_state": "Active", 
                            "received_prefix_count": -1, 
                            "remote_address": "172.16.0.80", 
                            "remote_as": 65080, 
                            "remote_port": 179, 
                            "remove_private_as": false, 
                            "router_id": "", 
                            "routing_table": "global", 
                            "suppress_4byte_as": true, 
                            "suppressed_prefix_count": -1, 
                            "up": false
                        }
                    ]
                }
            }
        }, 
        "changed": false, 
        "failed": false
    }
}
 [WARNING]: Could not create retry file '/home/mab/mab_automate/napalm/labs/04-napalm-ansible/lab_1/pb_get_facts.retry'.         [Errno 13] Permission denied: u'/home/mab/mab_automate/napalm/labs/04
-napalm-ansible/lab_1/pb_get_facts.retry'


PLAY RECAP *************************************************************************************************************************************************************************************************
arista1                    : ok=2    changed=0    unreachable=0    failed=0   
arista2                    : ok=0    changed=0    unreachable=0    failed=1   
vmx1                       : ok=2    changed=0    unreachable=0    failed=0   
vmx2                       : ok=0    changed=0    unreachable=0    failed=1   

mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ 
```

## Setters (configuration and validation commands):

### install_config:

```
mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ ansible-playbook lab_1/pb_cfg_bgp.yml 

PLAY [Configure BGP] ***************************************************************************************************************************************************************************************

TASK [Render BGP configuration] ****************************************************************************************************************************************************************************
fatal: [arista2]: FAILED! => {"changed": false, "failed": true, "msg": "AnsibleUndefinedVariable: 'local_asn' is undefined"}
fatal: [vmx2]: FAILED! => {"changed": false, "failed": true, "msg": "AnsibleUndefinedVariable: 'local_asn' is undefined"}
changed: [vmx1]
changed: [arista1]

TASK [Install rendered configuration] **********************************************************************************************************************************************************************
ok: [vmx1]
ok: [arista1]

PLAY [Wait for peers to establish connections] *************************************************************************************************************************************************************

TASK [pause] ***********************************************************************************************************************************************************************************************
Pausing for 18 seconds
(ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
ok: [localhost]

PLAY [Audit devices] ***************************************************************************************************************************************************************************************

TASK [Render validation files] *****************************************************************************************************************************************************************************
changed: [vmx1]
changed: [arista1]

TASK [Validate states] *************************************************************************************************************************************************************************************
ok: [arista1]
ok: [vmx1]
 [WARNING]: Could not create retry file '/home/mab/mab_automate/napalm/labs/04-napalm-ansible/lab_1/pb_cfg_bgp.retry'.         [Errno 13] Permission denied: u'/home/mab/mab_automate/napalm/labs/04
-napalm-ansible/lab_1/pb_cfg_bgp.retry'


PLAY RECAP *************************************************************************************************************************************************************************************************
arista1                    : ok=4    changed=2    unreachable=0    failed=0   
arista2                    : ok=0    changed=0    unreachable=0    failed=1   
localhost                  : ok=1    changed=0    unreachable=0    failed=0   
vmx1                       : ok=4    changed=2    unreachable=0    failed=0   
vmx2                       : ok=0    changed=0    unreachable=0    failed=1   

mab@mab-infra:~/mab_automate/napalm/labs/04-napalm-ansible$ 
```