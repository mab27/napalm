# NAPALM through CLI:
- This allows to consume the NAPALM library without writing any python script nor using any automation tool. This is a CLI you can use to directly interact with the network devices.
- Sections:
	- [Call methods](https://github.com/mab27/napalm/tree/master/labs/01-napalm-cli#call-methods)
		- [get_facts](https://github.com/mab27/napalm/tree/master/labs/01-napalm-cli#get_facts)
		- [get_bgp_config](https://github.com/mab27/napalm/tree/master/labs/01-napalm-cli#get_bgp_config)
		- [get_bgp_neigbors](https://github.com/mab27/napalm/tree/master/labs/01-napalm-cli#get_bgp_neigbors)		
	- [Call CLI](https://github.com/mab27/napalm/tree/master/labs/01-napalm-cli#call-cli)
	- [Configure](https://github.com/mab27/napalm/tree/master/labs/01-napalm-cli#configure)
		- [Example with Arista device]()
		- [Example with Juniper device]()
	- [Debug Mode](https://github.com/mab27/napalm/tree/master/labs/01-napalm-cli#debub-mode)


## Call methods:

### get_facts:

```
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 call get_facts
{
    "os_version": "4.18.1F-4591672.4181F", 
    "uptime": -689, 
    "interface_list": [
        "Ethernet1", 
        "Management1"
    ], 
    "vendor": "Arista", 
    "serial_number": "", 
    "model": "vEOS", 
    "hostname": "lon.arista1", 
    "fqdn": "lon.arista1"
}
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 call get_facts
{
    "os_version": "14.1R4.9", 
    "uptime": 6540, 
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
    "vendor": "Juniper", 
    "serial_number": "VM55E771B3CD", 
    "model": "VMX", 
    "hostname": "par.vmx1", 
    "fqdn": "par.vmx1"
}
mab@mab-infra:~$ 
```

### get_bgp_config:
```
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 call get_bgp_config
{
    "_": {
        "neighbors": {
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
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 call get_bgp_config
{
    "underlay": {
        "neighbors": {
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
                "description": "arista1"
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
mab@mab-infra:~$ 
```

### get_bgp_neigbors:
```
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 call get_bgp_neighbors
{
    "global": {
        "router_id": "70.70.70.70", 
        "peers": {
            "172.16.0.30": {
                "is_enabled": true, 
                "uptime": -2582, 
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
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 call get_bgp_neighbors
{
    "global": {
        "router_id": "30.30.30.30", 
        "peers": {
            "172.16.0.70": {
                "is_enabled": true, 
                "uptime": 4581, 
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
                "description": "arista1"
            }
        }
    }
}
mab@mab-infra:~$ 
```

## Call cli:

```
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 call cli --method-kwargs "commands=['show  version']"
{
    "show  version": "Arista vEOS\nHardware version:    \nSerial number:       \nSystem MAC address:  000c.29fa.c2c1\n\nSoftware image version: 4.18.1F\nArchitecture:           i386\nInternal build version: 4.18.1F-4591672.4181F\nInternal build ID:      6fcb426e-70a9-48b8-8958-54bb72ee28ed\n\nUptime:                 1 hour and 59 minutes\nTotal memory:           1891800 kB\nFree memory:            859976 kB\n\n"
}
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 call cli --method-kwargs "commands=['show  version']"
{
    "show  version": "\nHostname: par.vmx1\nModel: vmx\nJunos: 14.1R4.9\nJUNOS Base OS Software Suite [14.1R4.9]\nJUNOS Base OS boot [14.1R4.9]\nJUNOS Crypto Software Suite [14.1R4.9]\nJUNOS Online Documentation [14.1R4.9]\nJUNOS Kernel Software Suite [14.1R4.9]\nJUNOS Routing Software Suite [14.1R4.9]\nJUNOS Runtime Software Suite [14.1R4.9]\nJUNOS Services AACL PIC package [14.1R4.9]\nJUNOS Services Application Level Gateway [14.1R4.9]\nJUNOS Services Application Level Gateway (xlp64) [14.1R4.9]\nJUNOS Services Application Level Gateway (xlr64) [14.1R4.9]\nJUNOS AppId Services PIC Package [14.1R4.9]\nJUNOS Services AppId PIC package (xlr64) [14.1R4.9]\nJUNOS Border Gateway Function PIC package [14.1R4.9]\nJUNOS Services Captive Portal and Content Delivery PIC package [14.1R4.9]\nJUNOS Services HTTP Content Management PIC package [14.1R4.9]\nJUNOS Services HTTP Content Management PIC package (xlr64) [14.1R4.9]\nJUNOS IDP Services PIC Package [14.1R4.9]\nJUNOS Services JFLOW PIC package [14.1R4.9]\nJUNOS Services JFLOW PIC package (xlp64) [14.1R4.9]\nJUNOS Services LL-PDF PIC package [14.1R4.9]\nJUNOS MobileNext PIC package [14.1R4.9]\nJUNOS MobileNext PIC package (xlr64) [14.1R4.9]\nJUNOS Services Mobile Subscriber Service Container package [14.1R4.9]\nJUNOS Services Mobile Subscriber Service PIC package (xlr64) [14.1R4.9]\nJUNOS Services NAT PIC package [14.1R4.9]\nJUNOS Services NAT PIC package (xlp64) [14.1R4.9]\nJUNOS Services NAT PIC package (xlr64) [14.1R4.9]\nJUNOS Services PTSP PIC package [14.1R4.9]\nJUNOS Services RPM PIC package [14.1R4.9]\nJUNOS Services RPM PIC package (xlp64) [14.1R4.9]\nJUNOS Services Stateful Firewall PIC package [14.1R4.9]\nJUNOS Services Stateful Firewall PIC package (xlp64) [14.1R4.9]\nJUNOS Services Stateful Firewall PIC package (xlr64) [14.1R4.9]\nJUNOS BSG PIC package [14.1R4.9]\nJUNOS Services Crypto Base PIC package [14.1R4.9]\nJUNOS Services Crypto Base PIC package [14.1R4.9]\nJUNOS Services Crypto Base PIC package(xlr64) [14.1R4.9]\nJUNOS Services IPSec PIC package [14.1R4.9]\nJUNOS Services IPSec PIC package [14.1R4.9]\nJUNOS Services IPSec PIC(xlr64) package [14.1R4.9]\nJUNOS Services SSL PIC package [14.1R4.9]\nJUNOS Packet Forwarding Engine Trio Simulation Package [14.1R4.9]\n"
}
mab@mab-infra:~$ 
```

## Configure:

### Example with Arista device:

```
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 configure mab_automate/napalm/eos_new_config.txt --strategy merge --dry-run
@@ -27,6 +27,9 @@
    neighbor 172.16.0.30 remote-as 65030
    neighbor 172.16.0.30 description vmx1
    neighbor 172.16.0.30 maximum-routes 12000 
+   neighbor 172.16.0.40 remote-as 65040
+   neighbor 172.16.0.40 description vmx2
+   neighbor 172.16.0.40 maximum-routes 12000 
 !
 management api http-commands
    no shutdown
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 call get_bgp_config
{
    "_": {
        "neighbors": {
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
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 configure mab_automate/napalm/eos_new_config.txt --strategy merge
@@ -27,6 +27,9 @@
    neighbor 172.16.0.30 remote-as 65030
    neighbor 172.16.0.30 description vmx1
    neighbor 172.16.0.30 maximum-routes 12000 
+   neighbor 172.16.0.40 remote-as 65040
+   neighbor 172.16.0.40 description vmx2
+   neighbor 172.16.0.40 maximum-routes 12000 
 !
 management api http-commands
    no shutdown
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 call get_bgp_config
{
    "_": {
        "neighbors": {
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
mab@mab-infra:~$ napalm --user admin --password admin123 --vendor eos arista1 call get_bgp_neighbors
{
    "global": {
        "router_id": "70.70.70.70", 
        "peers": {
            "172.16.0.40": {
                "is_enabled": true, 
                "uptime": -7176, 
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
                "uptime": -1349, 
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
mab@mab-infra:~$ 
```

### Example with Junipers device:

```
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 configure mab_automate/napalm/junos_new_config.txt --strategy merge --dry-run
[edit protocols bgp group underlay]
      neighbor 172.16.0.70 { ... }
+     neighbor 172.16.0.80 {
+         description arista2;
+         peer-as 65080;
+     }
mab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 call get_bgp_config
{
    "underlay": {
        "neighbors": {
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
                "description": "arista1"
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
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 configure mab_automate/napalm/junos_new_config.txt --strategy merge 
[edit protocols bgp group underlay]
      neighbor 172.16.0.70 { ... }
+     neighbor 172.16.0.80 {
+         description arista2;
+         peer-as 65080;
+     }
mab@mab-infra:~$ 
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 call get_bgp_config
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
                "description": "arista2"
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
                "description": "arista1"
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
mab@mab-infra:~$ napalm --user mab --password mab123 --vendor junos vmx1 call get_bgp_neighbors
{
    "global": {
        "router_id": "30.30.30.30", 
        "peers": {
            "172.16.0.80": {
                "is_enabled": true, 
                "uptime": 27, 
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
                "description": "arista2"
            }, 
            "172.16.0.70": {
                "is_enabled": true, 
                "uptime": 604, 
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
                "description": "arista1"
            }
        }
    }
}
```


## Debub mode:
```
mab@mab-infra:~$ napalm --debug --user admin --password admin123 --vendor eos arista1 call cli --method-kwargs "commands=['show  version']"
2017-10-04 17:42:47,214 - napalm - DEBUG - Starting napalm's debugging tool
2017-10-04 17:42:47,214 - napalm - DEBUG - Gathering napalm packages
2017-10-04 17:42:47,221 - napalm - DEBUG - napalm-base==0.25.0
2017-10-04 17:42:47,221 - napalm - DEBUG - napalm-eos==0.6.1
2017-10-04 17:42:47,221 - napalm - DEBUG - napalm-fortios==0.4.0
2017-10-04 17:42:47,221 - napalm - DEBUG - napalm-ios==0.8.0
2017-10-04 17:42:47,221 - napalm - DEBUG - napalm-iosxr==0.5.4
2017-10-04 17:42:47,221 - napalm - DEBUG - napalm-junos==0.12.0
2017-10-04 17:42:47,221 - napalm - DEBUG - napalm-nxos==0.7.0
2017-10-04 17:42:47,222 - napalm - DEBUG - napalm-panos==0.4.0
2017-10-04 17:42:47,222 - napalm - DEBUG - napalm-pluribus==0.5.1
2017-10-04 17:42:47,222 - napalm - DEBUG - napalm-ros==0.2.2
2017-10-04 17:42:47,222 - napalm - DEBUG - napalm-vyos==0.1.3
2017-10-04 17:42:47,222 - napalm - DEBUG - napalm==1.2.0
2017-10-04 17:42:47,222 - napalm - DEBUG - get_network_driver - Calling with args: ('eos',), {}
2017-10-04 17:42:47,228 - napalm - DEBUG - get_network_driver - Successful
2017-10-04 17:42:47,228 - napalm - DEBUG - __init__ - Calling with args: (<class 'napalm_eos.eos.EOSDriver'>, 'arista1', 'admin'), {'password': u'*******', 'optional_args': {}, 'timeout': 60}
2017-10-04 17:42:47,228 - napalm - DEBUG - __init__ - Successful
2017-10-04 17:42:47,228 - napalm - DEBUG - pre_connection_tests - Calling with args: (<napalm_eos.eos.EOSDriver object at 0x7ff886c24a50>,), {}
2017-10-04 17:42:47,228 - napalm - DEBUG - open - Calling with args: (<napalm_eos.eos.EOSDriver object at 0x7ff886c24a50>,), {}
2017-10-04 17:42:47,326 - napalm - DEBUG - open - Successful
2017-10-04 17:42:47,326 - napalm - DEBUG - connection_tests - Calling with args: (<napalm_eos.eos.EOSDriver object at 0x7ff886c24a50>,), {}
2017-10-04 17:42:47,327 - napalm - DEBUG - get_facts - Calling with args: (<napalm_eos.eos.EOSDriver object at 0x7ff886c24a50>,), {}
2017-10-04 17:42:47,373 - napalm - DEBUG - Gathered facts:
{
    "os_version": "4.18.1F-4591672.4181F", 
    "uptime": 148, 
    "interface_list": [
        "Ethernet1", 
        "Management1"
    ], 
    "vendor": "Arista", 
    "serial_number": "", 
    "model": "vEOS", 
    "hostname": "lon.arista1", 
    "fqdn": "lon.arista1"
}
{
    "os_version": "4.18.1F-4591672.4181F", 
    "uptime": 148, 
    "interface_list": [
        "Ethernet1", 
        "Management1"
    ], 
    "vendor": "Arista", 
    "serial_number": "", 
    "model": "vEOS", 
    "hostname": "lon.arista1", 
    "fqdn": "lon.arista1"
}
2017-10-04 17:42:47,373 - napalm - DEBUG - get_facts - Successful
2017-10-04 17:42:47,373 - napalm - DEBUG - method - Calling with args: (<napalm_eos.eos.EOSDriver object at 0x7ff886c24a50>, 'cli'), {u'commands': ['show  version']}
2017-10-04 17:42:47,374 - napalm - DEBUG - cli - Attempting to resolve method
2017-10-04 17:42:47,374 - napalm - DEBUG - cli - Attempting to call method with kwargs: {u'commands': ['show  version']}
2017-10-04 17:42:47,404 - napalm - DEBUG - cli - Response
{
    "show  version": "Arista vEOS\nHardware version:    \nSerial number:       \nSystem MAC address:  000c.29fa.c2c1\n\nSoftware image version: 4.18.1F\nArchitecture:           i386\nInternal build version: 4.18.1F-4591672.4181F\nInternal build ID:      6fcb426e-70a9-48b8-8958-54bb72ee28ed\n\nUptime:                 2 hours and 2 minutes\nTotal memory:           1891800 kB\nFree memory:            859928 kB\n\n"
}
2017-10-04 17:42:47,404 - napalm - DEBUG - method - Successful
2017-10-04 17:42:47,404 - napalm - DEBUG - close - Calling with args: (<napalm_eos.eos.EOSDriver object at 0x7ff886c24a50>,), {}
2017-10-04 17:42:47,404 - napalm - DEBUG - close - Successful
2017-10-04 17:42:47,405 - napalm - DEBUG - post_connection_tests - Calling with args: (<napalm_eos.eos.EOSDriver object at 0x7ff886c24a50>,), {}
mab@mab-infra:~$ 
```

