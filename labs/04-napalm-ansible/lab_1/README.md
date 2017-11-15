# Lab_1

## Overview:
- Ansible playbooks using NAPALM modules
- Sections:
    - [Getters (show commands)]()
    	- [get_facts]()
      	- [get_bgp_config]()
    	- [get_bgp_neighbors]()
      	- [get_bgp_neighbors_detail]()
      	- [get_interfaces]()
      	- [get_interfaces_ip]()
      	- [get_interfaces_counters]()
      	- [get_lldp_neighbors]()
      	- [get_arp_table]()
      	- [ping]()
    - [Setters (configuration commands)]()
    	- [install_config]()

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

### get_bgp_config:
```

```

## Setters (configuration commands):

### install_config:

```

```
